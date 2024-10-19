from django.contrib import admin
from django.contrib.auth import views as auth_views 
from django.urls import path, include
from maps import views as user_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', user_views.logout_view, name='logout'),

    path("home/", user_views.HomePage, name = 'home'),
    path('admin/', admin.site.urls),
    path("addspot/", user_views.AddSpotPage, name = "addspot"),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

