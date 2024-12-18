from inicio.views import index
from django.urls import path

app_name = 'inicio'

urlpatterns = [
    path('', index, name='index'),
]
