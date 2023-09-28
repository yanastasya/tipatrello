
from faker import Faker
import random

fake = Faker(locale="ru_RU")
fake.random.seed(4321)
count = 0
#for i in range(5):
   # random_text = fake.text()[:500]
   # print(random_text)

print(random.randint(0, 100))   
    