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


    

