from csv import DictReader

from django.core.management import BaseCommand

from projects.models import Worker
import random
from random import shuffle
from faker import Faker

  

class Command(BaseCommand):
    # Show this when the user types help
    help = "Загрузка данных о сотрудниках.(тестовые данные о 1000 сотрудниках будут сгенерированы случайным образом)"

    def handle(self, *args, **options):

        print("Загрузка...")
        fake = Faker(locale="ru_RU")
        fake.random.seed(4321)        
        for i in range(20):
            random_name = fake.name().split() 
            worker = Worker(
                surname=random_name[0],
                name=random_name[1],
                patronymic=random_name[2],
                position=fake.job()
            )
            worker.save()        

        print(f'Тестовые данные о сотрудниках успешно загружены')