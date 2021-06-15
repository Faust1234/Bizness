from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import requests

from .forms import Userregistarions

@login_required
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q=las%20vegas&units=imperial&appid=3b212a2a8d80257d845ca625a25c1522'
    city = 'las Vegas'

    city_weather = requests.get(url.format(city)).json()

    print(city_weather)
    return render(request, 'user/index.html')

def register(request):
    if request.method == 'POST':
        form = Userregistarions(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You log in')
            return redirect('index')


    else:
        form = Userregistarions()

    return render(request, 'user/register.html', {'form': form})