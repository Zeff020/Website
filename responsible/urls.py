from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.responsible, name='responsible-eramet'),
]