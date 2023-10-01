from django.urls import path
from . import views

app_name = 'projects'

urlpatterns = [
    path('', views.index, name='index'),
    path('task/<int:task_id>/', views.TaskDetail, name='task-detail'),
    path(
        'task/<int:task_id>/comment/', views.add_comment, name='add_comment'),

]
