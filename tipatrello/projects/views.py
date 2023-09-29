from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Project,Task,Worker
from .utils import get_page
from .form import CommentForm

def index(request):   

    template = 'index.html'
    project_list = Project.objects.all()
    #page_obj = get_page(request, project_list)
    context = {
        'page_obj': project_list,
    }

    return render(request, template, context)


def TaskDetail(request, task_id):
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

    task = get_object_or_404(Task, id=task_id)
    form = CommentForm(request.POST or None)
    
    comment = form.save(commit=False)        
    comment.task = task
    comment.save()

    return redirect('projects:task-detail', task.id)
