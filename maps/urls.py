from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage, name="maps"),
    path("<int:item_id>/", views.SpotPage, name="spot detials")
]
