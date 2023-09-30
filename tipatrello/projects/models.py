from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.urls import reverse
import datetime

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
        return f'{self.surname} {self.name} - {self.position}'


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
    #tasks = models.ManyToManyField(
        #Task,     
        #verbose_name='Задачи проекта',       
        #related_name='projects',
    #)

    is_active = models.BooleanField(
        default=True,
        db_index=True, 
    )
    pub_date = models.DateTimeField(
        'Дата создания',      
        null = True,       
        auto_now_add=True
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return self.name


class Task(MPTTModel):
    "Связь сотрудника с конкретной задачей."
    TASK_STATUS = [
        ('Новая', 'Новая'),
        ('В работе', 'В работе'),
        ('Закрыта', 'Закрыта'),
    ]
    name = models.CharField(
        'Название задачи',
        max_length=50,
    )
    status = models.CharField(
        'Статус задачи',
        choices=TASK_STATUS,
        default='Новая',
        max_length=10,
    )
    parent = TreeForeignKey(
        'self',
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name='children',
        db_index=True,
        verbose_name='Надзадача'
    )       
    description = models.TextField(
        'Описание задачи',
        max_length=500,
    )
    workers = models.ManyToManyField(
        Worker,
        blank=True,               
        related_name='task_and_workers',
        verbose_name='исполнитель задачи',
    )
    project = models.ForeignKey(
        Project,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='tasks',
        verbose_name='Относится к проекту',        
    )   

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    class MPTTMeta:
        order_insertion_by = ['name']    

    def get_absolute_url(self):
        return reverse('projects:task-detail', args=[str(self.id)])
    
    def __str__(self):
        return self.name



class Comment(models.Model):
    """Комментирование задач."""
    task = models.ForeignKey(
        Task,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Комментарий',
    )
    pub_date = models.DateTimeField(
        'Дата создания',
        auto_now_add=True
    )
    text = models.TextField(
        'Текст',
    )

    class Meta:
        ordering = ['-pub_date']
        verbose_name = 'Комментарий к задаче'
        verbose_name_plural = 'Комментарии к задаче'

    def __str__(self):
        return self.text
