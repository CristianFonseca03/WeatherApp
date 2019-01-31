# Django
from django.shortcuts import render, redirect
from Weather.settings.base import BASE_DIR

# Python
from urllib.request import urlopen
import json
import pytemperature
import os



def start_view(request):
    """Start View."""
    if request.method == 'POST':
        lat = request.POST['lat']
        lon = request.POST['lon']
        if lat == '0' or lon == '0':
            return render(request, 'home.html', {'error': 'Seleccione una cuidad'})
        return redirect('weather', coordinates=lat + ',' + lon)
    return render(request, 'home.html')

def get_day_status(icon):
    status = False
    if "n" in icon:
        status = True
    return status

def weather(request, coordinates):
    x = coordinates.split(',')
    url = 'http://api.openweathermap.org/data/2.5/weather?lat=' + x[0] + '&lon=' + x[
        1] + '&APPID=AIzaSyD-rw5J8sP6hSnr2JVTR0U_B7n4d4Z2cuI'
    response = urlopen(url)
    data = json.load(response)
    code = data['weather'][0]['id']
    main = data['weather'][0]['main']
    temp = data['main']['temp']
    icon_code = data['weather'][0]["icon"]
    temp2c = pytemperature.k2c(temp)
    try:
        country = data['sys']['country']
    except KeyError:
        country = "NN"
    city_name = data['name']
    template = 'weather.html'
    icons = json.loads(open(os.path.join(BASE_DIR, '../static/icons.json')).read())
    if get_day_status(icon_code):
        status="night"
        icon = icons[str(code)]['icon_night']
    else:
        icon = icons[str(code)]['icon_day']
        status="day"
    description = icons[str(code)]['description_es']
    try:
        main_es = icons["descriptions"][main]
    except KeyError:
        main_es=main
    context = {
        'main': main_es,
        'temp': int(temp2c),
        'country': country,
        'city_name': city_name,
        'icon': icon,
        'description': description,
        'status':status
    }
    return render(request, template, context)