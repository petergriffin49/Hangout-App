from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import *
from .forms import *

# [log in crap]
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
    context = {
        
    }
    template = loader.get_template("Home.html")
    return HttpResponse(template.render(context,request))
