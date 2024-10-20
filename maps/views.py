from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.urls import reverse_lazy 
from django.views.generic import ListView, CreateView
from math import *
from .models import *
from .forms import *

# [LOG IN CRAP (not used rn)]
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your account has been created. You can log in now!')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'user/register.html', context)

def logout_view(request):
    logout(request)
    return redirect('login')

# [home screen]
def HomePage(request):
    spot_list = Spot.objects.all()
    cord_list = Spot.objects.all().values('spot_name','spot_latitude','spot_longitude') # context for javascript (map marker creation)
    context = {
        "spots": list(spot_list),
        "cords": list(cord_list),
    }
    template = loader.get_template("Map.html")
    return HttpResponse(template.render(context, request))


# specific spot screen (same shit as home basically)
def SpotPage(request, spot_id):
    spot_list = Spot.objects.filter(id=spot_id)
    cord_list = Spot.objects.filter(id=spot_id).values('spot_name','spot_latitude','spot_longitude') # context for javascript (map marker creation)
    context = {
        "spots": list(spot_list),
        "cords": list(cord_list),
    }
    template = loader.get_template("MapSpot.html")
    return HttpResponse(template.render(context, request))


# [add spot screen with premade form class] (used)
def AddSpotPage2(request):
    if request.method == 'POST':
        form = SpotForm(request.POST, request.FILES)  # Include request.FILES
        if form.is_valid():
            form.save()  # Save the new object
            return redirect('home')  # Redirect to a success page
    else:
        form = SpotForm()
    
    return render(request, 'AddSpot.html', {'form': form})

# [add page screen] (UNused)
def AddSpotPage(request):
    template = loader.get_template("AddSpot.html")
    context = {}

    if (request.GET.get("getSpot")):
        name = request.GET.get("SpotName")
        desc = request.GET.get("SpotDescription")
        lat = request.GET.get("Latitude")
        lon = request.GET.get("Longitude")

        ph = request.GET.get("img")
        photo_data = InMemoryUploadedFile(
            file=request.FILES['image'], 
            field_name='image', 
            name='image.jpg', 
            content_type='image/jpeg', 
            size=len(request.FILES['image'].read()), 
            charset=None
        )
    
        Spot.objects.bulk_create([Spot(spot_name=name, spot_description=desc, spot_latitude=lat, spot_longitude=lon, photo=photo_data)])
        return redirect("/home")   
    
    return HttpResponse(template.render(context, request))  




    
        