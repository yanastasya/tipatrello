from django.core.management import BaseCommand
from faker import Faker

from projects.models import Worker


class Command(BaseCommand):
    """Команда для заполнения данными таблицы Workers (сотрудники.)"""
    
    help = (
        "Загрузка данных о сотрудниках",
        "(тестовые данные о 1000 сотрудниках будут",
        "сгенерированы случайным образом)."
    )

    def handle(self, *args, **options):
        print("Загрузка данных о сотрудниках....")
        fake = Faker(locale="ru_RU")
        fake.random.seed(4321)
        for i in range(1000):
            random_name = fake.name().split()
            worker = Worker(
                surname=random_name[0],
                name=random_name[1],
                patronymic=random_name[2],
                position=fake.job()
            )
            worker.save()

        print('Тестовые данные о сотрудниках успешно загружены.')
