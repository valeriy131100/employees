from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers


def index(request):
    return render(
        request,
        template_name='index.html'
    )
