from django.urls import path
from . import views

urlpatterns = [
    path('reservas', views.index),
    path('instalaciones', views.facilities)
]
