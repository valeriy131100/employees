from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers

from .models import Employee


def index(request):
    return render(
        request,
        template_name='index.html'
    )


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = (
            'id',
            'full_name',
            'position',
            'employment_date',
            'salary'
        )


@api_view(['GET'])
def get_subordinates(request, start_from=None):
    if start_from is None:
        employees = Employee.objects.filter(boss=None)
    else:
        print(start_from)
        boss = get_object_or_404(Employee, pk=start_from)
        employees = boss.subordinates

        print(boss.subordinates)

    return Response(
        EmployeeSerializer(
            employees,
            many=True
        ).data
    )
