import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest19_pagination.settings')
import django
django.setup()
from testapp.models import Employee
from faker import Faker
fake = Faker('en_IN')
import random
def emp_data(n=120):
    for i in range(n):
        eno = random.randrange(102, 999)
        ename = fake.name()
        esal = random.randrange(10000, 90000)
        eaddr = fake.city()
        emps = Employee.objects.get_or_create(eno=eno, ename=ename, esal=esal, eaddr=eaddr)
emp_data()
