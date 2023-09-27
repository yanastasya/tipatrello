from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Здесь будет древовидный список проектов с задачами")

# Create your views here.





