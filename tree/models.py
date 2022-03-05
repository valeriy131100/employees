from django.db import models


class Employee(models.Model):
    full_name = models.CharField(
        verbose_name='ФИО',
        max_length=200,
        db_index=True
    )
    position = models.CharField(
        verbose_name='Должность',
        max_length=200,
        db_index=True
    )
    employment_date = models.DateField(
        verbose_name='Дата трудоустройства',
        db_index=True
    )
    boss = models.ForeignKey(
        'Employee',
        verbose_name='Начальник',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    def __str__(self):
        return f'{self.full_name}: {self.position}'
