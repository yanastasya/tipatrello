import random
from faker import Faker

from django.core.management import BaseCommand

from projects.models import Worker, Task, Project


class Command(BaseCommand):
    """Команда для заполнения данными таблицы Task (задачи.),
    без прикрепления к проектам."""

    help = (
        "Загрузка данных о задачах",
        "(тестовые данные о 10000 задачах будут",
        "сгенерированы случайным образом)."
    )

    def handle(self, *args, **options):

        print("Загрузка данных о задачах")
        fake = Faker(locale="ru_RU")
        fake.random.seed(4321)

        for i in range(10000):
            random_text = fake.text()
            task = Task(
                name=f'Задача {i}',
                description=random_text[:500],
                project=Project.objects.get(id=random.randint(1, 250)),
                status='Новая'
            )
            task.save()
            task.workers.add(
                Worker.objects.get(id=random.randint(1, 250)),
                Worker.objects.get(id=random.randint(200, 600)),
                Worker.objects.get(id=random.randint(350, 750)),
                Worker.objects.get(id=random.randint(600, 1000)),
            )

        print('Тестовые данные о задачах успешно загружены')
