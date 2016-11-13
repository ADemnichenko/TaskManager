import string
import random
from django.utils import timezone
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .models import Task, Progress, Prioritet, Clases

# Create your views here.

def base(request):
    if request.user.is_anonymous:
        return redirect('/admin')
    circle_count = range(7)

    controls_list = ["task_del", "task_complete", "task_start"]
    task_lists = ["open", "in_process","closed"]

    in_process = get_task_in_process(request, Progress.objects.get(flag='in process'))
    closed = get_closed_tasks(request, Progress.objects.get(flag='closed'))
    open = get_open_tasks(request, Progress.objects.get(flag='open'))
    hot = Prioritet.objects.get(prioritet='hot')
    prioritet = get_prioritet_tasks(request, Prioritet.objects.get(prioritet='hot'), Progress.objects.get(flag='open'))

    return render(request, 'TskMng/base.html', {'hot': hot, 'open': open, 'closed': closed,
                                                     'in_process': in_process, 'circle_count': circle_count,
                                                     'controls_list':controls_list, 'task_lists':task_lists, 'prioritet':prioritet})


def get_prioritet_tasks(request, hot, flag):
    if request.user.is_superuser:
        task = Task.objects.filter(task_progress=flag, task_prioritet=hot)
    else:
        task = Task.objects.filter(task_progress=flag, task_prioritet=hot, task_author=request.user)
    return task

def get_task_in_process(request, in_process):
    if request.user.is_superuser:
        task = Task.objects.filter(task_progress=in_process)
    else:
        task = Task.objects.filter(task_progress=in_process, task_author=request.user)
    return task.order_by('-task_in_process')


def get_open_tasks(request, open):
    if request.user.is_superuser:
        task = Task.objects.filter(task_progress=open)
    else:
        task = Task.objects.filter(task_progress=open, task_author=request.user)
    return task.order_by('-task_open')


def get_closed_tasks(request, closed):
    if request.user.is_superuser:
        task = Task.objects.filter(task_progress=closed)
    else:
        task = Task.objects.filter(task_progress=closed, task_author=request.user)
    return task.order_by('-task_closed')


def task_del(request, pk):
    delete = get_object_or_404(Task, pk=pk)
    delete.delete()
    return redirect('base')


def task_complete(request, pk):
    process = Progress.objects.get(flag='closed')
    complete = get_object_or_404(Task, pk=pk)
    complete.task_progress = process
    complete.task_closed = timezone.now()
    complete.save(update_fields=['task_progress', 'task_closed'])
    return redirect('base')


def task_start(request, pk):
    process = Progress.objects.get(flag='in process')
    start = get_object_or_404(Task, pk=pk)
    start.task_progress = process
    start.task_in_process = timezone.now()
    start.save(update_fields=['task_progress', 'task_in_process'])
    return redirect('base')


def auto_generator(request):
    # --------AUTO GEMERATE TASKS-----------
    flags = Progress.objects.all()
    prioritets = Prioritet.objects.all()
    clases = Clases.objects.all()
    auth = User.objects.all()
    counter = 0
    for i in range(0, 10):
        my_rand_descr = ""
        for i in range(random.randint(30, 300)):
            counter += 1
            if counter == 60:
                my_rand_descr += "\n"
                counter = 0
            else:
                my_rand_descr += "".join(random.choice(string.ascii_uppercase + string.digits))

        Task.objects.create(task_author=random.choice(auth), task_name=random.choice(clases),
                            task_description=my_rand_descr,
                            task_progress=random.choice(flags), task_prioritet=random.choice(prioritets),
                            task_class=random.choice(clases))
        # ---------------------------------------------
    return redirect('base')
