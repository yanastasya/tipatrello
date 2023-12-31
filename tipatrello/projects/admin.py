from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Worker, Task, Project, Comment


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'surname', 'name', 'patronymic', 'position'
    )


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class TaskInline(admin.TabularInline):
    model = Task
    extra = 0


@admin.register(Task)
class TaskAdmin(MPTTModelAdmin):
    inlines = [CommentInline]
    list_display = (
        'id', 'name', 'description', 'status',
    )


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [TaskInline]
    list_display = (
       'id', 'name', 'deadline', 'chief', 'is_active',
    )


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'text', 'pub_date', 'task',
    )
