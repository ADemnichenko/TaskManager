from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
import string
from .models import Task, Progress, Prioritet, Clases
import random
# Create your views here.
def task_list(request):
    circle_count = range(7)
    counter = 1
    flag_open = Progress.objects.get(flag = 'open')
    flag_closed = Progress.objects.get(flag='closed')
    flag_in_process = Progress.objects.get(flag='in process')
    prioritet_hot = Prioritet.objects.get(prioritet='hot')
    user =  User.objects.get(username = "Admin")
    if request.user == user:
        tasks_open = Task.objects.filter(task_progress=flag_open)
        tasks_prioritet = Task.objects.filter(task_progress=flag_open, task_prioritet=prioritet_hot)
        tasks_closed = Task.objects.filter(task_progress=flag_closed)
        task_in_progres = Task.objects.filter(task_progress=flag_in_process)
    else:
        tasks_open = Task.objects.filter(task_progress = flag_open, task_author = request.user)
        tasks_prioritet = Task.objects.filter(task_progress = flag_open, task_prioritet=prioritet_hot, task_author=request.user)
        tasks_closed = Task.objects.filter(task_progress = flag_closed, task_author = request.user)
        task_in_progres = Task.objects.filter(task_progress = flag_in_process, task_author = request.user)
    return render(request, 'TskMng/task_list.html', {'prioritet_hot':prioritet_hot,'tasks_prioritet': tasks_prioritet,'tasks_open': tasks_open,'tasks_closed':tasks_closed, 'task_in_progres':task_in_progres, 'circle_count': circle_count, 'counter':counter})

def task_del(request, pk):
    task_delete = get_object_or_404(Task, pk=pk)
    task_delete.delete()
    return redirect('task_list')

def task_complete(request, pk):
    flag_closed = Progress.objects.get(flag='closed')
    task_complete = get_object_or_404(Task, pk=pk)
    task_complete.task_progress = flag_closed
    task_complete.save(update_fields=['task_progress'])
    return redirect('task_list')

def task_start(request, pk):
    flag_in_process = Progress.objects.get(flag='in process')
    task_start = get_object_or_404(Task, pk=pk)
    task_start.task_progress = flag_in_process
    task_start.save(update_fields=['task_progress'])
    return redirect('task_list')

def auto_generator(request):
    # --------AUTO GEMERATE TASKS-----------
    flags = Progress.objects.all()
    prioritets = Prioritet.objects.all()
    clases = Clases.objects.all()
    auth = User.objects.all()
    counter = 0
    for i in range(0,10):
        my_rand_descr = ""
        for i in range(random.randint(30, 300)):
            counter += 1
            if counter == 40:
                my_rand_descr += "\n"
                counter = 0
            else:
                my_rand_descr += "".join(random.choice(string.ascii_uppercase + string.digits))

        Task.objects.create(task_author = random.choice(auth), task_name=random.choice(clases),
                            task_description=my_rand_descr,
                            task_progress=random.choice(flags), task_prioritet=random.choice(prioritets),
                            task_class=random.choice(clases))
        # ---------------------------------------------
    return redirect('task_list')