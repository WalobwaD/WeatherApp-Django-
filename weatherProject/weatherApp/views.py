import json
import math
from django.shortcuts import render
import requests
import json
from .forms import cityForm
from .models import *
# Create your views here.
def home_view(request):
    
    if request.method == 'POST':
        form = cityForm(request.POST)
        
        if form.is_valid():
            form.save()
    form = cityForm()
    
    cities = City.objects.all()
    
    weather_data = []
    
    source = 'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=4ea1e050c60c08cf42ec0a5ce451d030'
    
    for city in cities:
    
        datas= requests.get(source.format(city)).json()
        
        data = {
            'city' : city.city_name,
            'country_name' : str(datas['sys']['country']),
            'position' : str(datas['coord']['lon']) + ' ' + str(datas['coord']['lat']),
            'current_weather' : str(datas['weather'][0]['main']),
            'weather_icon' : str(datas['weather'][0]['icon']),
            'current_temp' : str(math.floor(datas['main']['temp'])),
            'current_press' : str(datas['main']['pressure']),      
            'desc' : str(datas['weather'][0]['description']),    
            }
        weather_data.append(data)

    context = {
        'cities' : weather_data,
        'form' : form,
        }

    return render(request, 'weatherApp/home.html', context)


# def home_view(request):
    
#     if request.method == 'POST':
#         city = request.POST['city']
#         source = urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&appid=4ea1e050c60c08cf42ec0a5ce451d030').read()
#         datas= json.loads(source)
#         data = {
#             'country_name' : str(datas['sys']['country']),
#             'position' : str(datas['coord']['lon']) + ' ' + str(datas['coord']['lat']),
#             'current_weather' : str(datas['weather'][0]['main']),
#             'weather_icon' : str(datas['weather'][0]['icon']),
#             'current_temp' : str(datas['main']['temp']),
#             'current_press' : str(datas['main']['pressure']),      
#             'desc' : str(datas['weather'][0]['description']),    
#         }
#         print(data)
#     else:
#         data = {}
        

#     return render(request, 'weatherApp/home.html', data)