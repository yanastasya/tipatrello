from django.core.management import BaseCommand

import random
from faker import Faker

from projects.models import Worker, Project


class Command(BaseCommand):
    """Команда для заполнения данными таблицы Projects (Проекты)"""
    help = (
        "Загрузка данных о проектах",
        "(тестовые данные о 250 проектах будут",
        "сгенерированы случайным образом)."
    )

    def handle(self, *args, **options):

        print("Загрузка данных о проектах")
        fake = Faker(locale="ru_RU")
        fake.random.seed(4321)

        for i in range(250):
            random_text = fake.text()
            random_date = fake.future_date()

            project = Project(
                name=f'Проект {i}',
                description=random_text[:500],
                is_active=True,
                chief=Worker.objects.get(id=random.randint(0, 1000)),
                deadline=random_date,
            )
            project.save()

        print('Тестовые данные о задачах успешно загружены')
