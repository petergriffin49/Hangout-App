from django.urls import path
from . import views

urlpatterns = [
    path("", views.HomePage, name="maps"),
<<<<<<< Updated upstream
=======
    path("<int:spot_id>/", views.SpotPage, name="spot home"),
>>>>>>> Stashed changes
]
