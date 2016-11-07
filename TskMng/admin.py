from django.contrib import admin
from .models import  Task, Progress, Prioritet, Clases
# Register your models here.
admin.site.register(Task)
admin.site.register(Progress)
admin.site.register(Prioritet)
admin.site.register(Clases)
