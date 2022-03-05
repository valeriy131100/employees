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
                employment_date=fake.date(),
                salary=random.randint(100, 50000)
            )
            for _ in range(50000)
        ]

        Employee.objects.bulk_create(employees)

        for num, employee in enumerate(employees):
            if num >= 10:
                employee.boss = employees[num//10 - 1]

        Employee.objects.bulk_update(employees, fields=['boss'])
