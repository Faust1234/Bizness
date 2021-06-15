from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import requests

from .models import City
from .forms import Userregistarions, CityForm

@login_required
def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3b212a2a8d80257d845ca625a25c1522'
    city = 'Las Vegas'

    cities = City.objects.all()

    form = CityForm

    if request.method == 'POST':  # only true if form is submitted
        form = CityForm(request.POST)  # add actual request data to form for processing
        form.save()

    weather_data = []

    for city in cities:
        city_weather = requests.get(
            url.format(city)).json()  # request the API data and convert the JSON to Python data types

        weather = {
            'city': city,
            'temperature': city_weather['main']['temp'],
            'description': city_weather['weather'][0]['description'],
            'icon': city_weather['weather'][0]['icon']
        }

        weather_data.append(weather)

    context = {'weather': weather_data}

    return render(request, 'user/index.html', context)

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