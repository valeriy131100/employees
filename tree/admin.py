from django.contrib import admin

from .models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    raw_id_fields = ['boss']
    list_display = [
        'full_name',
        'position',
        'salary',
        'employment_date',
        'boss'
    ]
