from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
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


# [add page screen]
def AddSpotPage(request):
    template = loader.get_template("AddSpot.html")
    ## No context... YET
    context = {}
    return HttpResponse(template.render(context, request))


