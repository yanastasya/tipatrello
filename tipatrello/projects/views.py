from django.shortcuts import render
from django.http import HttpResponse
from .models import Project,Task,Worker
from .utils import get_page

def index(request):   

    template = 'index.html'
    project_list = Project.objects.all()
    page_obj = get_page(request, project_list)
    context = {
        'page_obj': page_obj,
    }

    return render(request, template, context)




