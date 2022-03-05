from django.urls import path

from .views import index, get_subordinates

urlpatterns = [
    path('', index, name='index'),
    path('api/subordinates/', get_subordinates, name='root_subordinates'),
    path(
        'api/subordinates/<int:start_from>/',
        get_subordinates,
        name='subordinates'
    )
]
