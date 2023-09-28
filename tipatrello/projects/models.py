from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse

class Worker(models.Model):
    "Данные о сотрудниках."
    surname = models.CharField(
        'Фамилия',
        max_length=20
    )
    name = models.CharField(
        'Имя',
        max_length=20
    )    
    patronymic = models.CharField(
        'Отчество',
        max_length=20
    )
    position = models.CharField(
        'Должность',
        max_length=20
    )

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.name  


class Task(models.Model):
    "Связь сотрудника с конкретной задачей."
    
    name = models.CharField(
        'Название задачи',
        max_length=50,
    )
    is_done = models.BooleanField()
    
    description = models.TextField(
        'Описание задачи',
        max_length=500,
    )

    workers = models.ManyToManyField(
        Worker,               
        related_name='task_and_workers',
        verbose_name='исполнитель задачи',
    )    
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.name


class Project(models.Model):    

    name = models.CharField(
        'Название проекта',
        max_length=20,
    )
    deadline = models.DateField(
        'Срок исполнения',
    )
    description = models.TextField(
        'Описание проекта',
        max_length=500,
    )
    chief = models.ForeignKey(        
        Worker,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='project_as_chief',
        verbose_name='Руководитель проекта',
    )    
    tasks = models.ManyToManyField(
        Task,        
        #on_delete=models.DO_NOTHING, #если удаляют задачу, то ничего не происходит
        #related_name='project',
        verbose_name='Задачи проекта',       
        related_name='projects',
    )

    is_done = models.BooleanField()

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name
