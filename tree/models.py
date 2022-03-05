from django.db import models


class Employee(models.Model):
    full_name = models.CharField(
        verbose_name='ФИО',
        max_length=200
    )
    position = models.CharField(
        verbose_name='Должность',
        max_length=200
    )
    employment_date = models.DateField(
        verbose_name='Дата трудоустройства'
    )
    boss = models.ForeignKey(
        'Employee',
        verbose_name='Начальник',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
