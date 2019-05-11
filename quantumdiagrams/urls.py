from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.quantumdiagrams, name='quantumdiagrams'),
]