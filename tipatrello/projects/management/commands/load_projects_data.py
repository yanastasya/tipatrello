from csv import DictReader

from django.core.management import BaseCommand

from projects.models import Worker, Task, Project
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
        n=5    
        for i in range(25):
            random_text = fake.text()
            random_date = fake.date()        
                  
            project = Project(                
                name=f'Проект {i}',
                description=random_text[:500],
                is_done = False,
                chief=Worker.objects.get(id=random.randint(0, 19)),
                deadline = random_date,
            )
            project.save()
            
            for j in range(n,(n+5)):
                #print(f'id задачи {}')
                project.tasks.add(
                    Task.objects.get(id=j),
                )
        n+=5        

                    

        print(f'Тестовые данные о задачах успешно загружены')