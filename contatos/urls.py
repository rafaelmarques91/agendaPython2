from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:idContato>', views.showContato, name='showContato'),
]
