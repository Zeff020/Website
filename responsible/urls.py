from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.landingpage, name='thegreenprint-landingpage'),
    path('main/', views.main, name ='thegreenprint-main')
]