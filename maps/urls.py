from django.urls import path
from . import views
from .views import CreatePostView 

urlpatterns = [
    path("", views.HomePage, name="maps"),
    path("<int:spot_id>/", views.SpotPage, name="spot home"),
]
