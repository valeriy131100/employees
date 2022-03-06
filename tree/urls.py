from django.urls import path

from .views import index, get_subordinates, tree

urlpatterns = [
    path('', index, name='index'),
    path('tree/', tree, name='tree'),
    path('api/subordinates/', get_subordinates, name='root_subordinates'),
    path(
        'api/subordinates/<int:start_from>/',
        get_subordinates,
        name='subordinates'
    )
]
