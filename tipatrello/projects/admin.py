from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Worker, Task, Project

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'id','surname', 'name', 'patronymic', 'position'
    ) 


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id','name', 'description', 'is_done',
    )



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):    
    list_display = (
        'name', 'deadline', 'chief', 'is_done'
    )    




