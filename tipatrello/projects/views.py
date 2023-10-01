from django.shortcuts import render, get_object_or_404, redirect

from .models import Project, Task
from .form import CommentForm


def index(request):
    "Главная страница со списком проектов."
    template = 'index.html'
    project_list = Project.objects.all()
    context = {
        'page_obj': project_list,
    }

    return render(request, template, context)


def TaskDetail(request, task_id):
    "Страница с детальной информацией о задаче."
    template = 'task_detail.html'
    task = get_object_or_404(
        Task.objects, id=task_id
    )
    form = CommentForm(request.POST or None)
    comments = task.comments.all()

    context = {
        'task': task,
        'comments': comments,
        'form': form,
    }

    return render(request, template, context)


def add_comment(request, task_id):
    "Создание комментария к задаче."
    task = get_object_or_404(Task, id=task_id)
    form = CommentForm(request.POST or None)
    
    comment = form.save(commit=False)
    comment.task = task
    comment.save()

    return redirect('projects:task-detail', task.id)
