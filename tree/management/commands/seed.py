import random

from django.conf import settings
from django.core.management.base import BaseCommand
from faker import Faker
from faker.providers import job as fake_job, date_time as fake_date

from tree.models import Employee


class Command(BaseCommand):
    help = 'Seed employees data'

    def handle(self, *args, **options):
        fake = Faker([settings.LANGUAGE_CODE])
        fake.add_provider(fake_job)
        fake.add_provider(fake_date)

        employees = [
            Employee(
                full_name=fake.name(),
                position=fake.job(),
                employment_date=fake.date()
            )
            for i in range(50000)
        ]

        Employee.objects.bulk_create(employees)

        for num, employee in enumerate(employees):
            if 10 <= num < 100:
                employee.boss = random.choice(employees[0:10])
            if 100 <= num < 1000:
                employee.boss = random.choice(employees[10: 100])
            if 1000 <= num < 10000:
                employee.boss = random.choice(employees[1000:10000])
            if 10000 <= num <= 50000:
                employee.boss = random.choice(employees[1000:10000])

        Employee.objects.bulk_update(employees, fields=['boss'])

