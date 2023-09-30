from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Worker, Task, Project, Comment
from mptt.admin import MPTTModelAdmin

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'id','surname', 'name', 'patronymic', 'position'
    ) 


@admin.register(Task)
class TaskAdmin(MPTTModelAdmin):
    list_display = (
        'id','name', 'description', 'status',
    )

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):    
    list_display = (
        'name', 'deadline', 'chief', 'is_active'
    )    


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):    
    list_display = (
        'text', 'pub_date', 'task',
    )    


