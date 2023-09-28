from csv import DictReader

from django.core.management import BaseCommand

from projects.models import Worker, Task
import random
from random import shuffle
from faker import Faker

  

class Command(BaseCommand):
    # Show this when the user types help
    help = "Загрузка данных о сотрудниках.(тестовые данные о 1000 сотрудниках будут сгенерированы случайным образом)"

    def handle(self, *args, **options):

        print("Загрузка данных о задачах")
        fake = Faker(locale="ru_RU")
        fake.random.seed(4321) 
            
        for i in range(10005):
            random_text = fake.text()           
                      
            task = Task(                
                name=f'Задача {i}',
                description=random_text[:500],
                is_done = False,
                #workers=Worker.objects.get(id=random.randint(0, 1000)),
            )
            task.save()
            task.workers.add(
                Worker.objects.get(id=random.randint(6, 500)),
                Worker.objects.get(id=random.randint(100, 600)),
                Worker.objects.get(id=random.randint(200, 800)),
                Worker.objects.get(id=random.randint(400, 1005)),
            )

                    

        print(f'Тестовые данные о задачах успешно загружены')