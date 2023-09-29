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
        return f'{self.surname} {self.name} - {self.position}'


class Task(MPTTModel):
    "Связь сотрудника с конкретной задачей."
    
    name = models.CharField(
        'Название задачи',
        max_length=50,
    )
    is_done = models.BooleanField()

    parent = TreeForeignKey(
        'self',
        on_delete=models.PROTECT,
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

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    class MPTTMeta:
        order_insertion_by = ['name']    

    def get_absolute_url(self):
        return reverse('projects:task-detail', args=[str(self.id)])
    
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
        verbose_name='Задачи проекта',       
        related_name='projects',
    )

    is_done = models.BooleanField()

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

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
