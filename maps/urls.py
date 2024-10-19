from django.urls import path
from . import views

urlpatterns = [
    path("", views.Controlroom, name="maps"),
]
