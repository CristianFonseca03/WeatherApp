# Django
from django.shortcuts import render, redirect
from Weather.settings.base import BASE_DIR

# Python
from urllib.request import urlopen
import json
import pytemperature
import os
import goslate

gs = goslate.Goslate()


def start_view(request):
    """Start View."""
    if request.method == 'POST':
        lat = request.POST['lat']
        lon = request.POST['lon']
        if lat == '0' or lon == '0':
            return render(request, 'home.html', {'error': 'Seleccione una cuidad'})
        return redirect('weather', coordinates=lat + ',' + lon)
    return render(request, 'home.html')


def weather(request, coordinates):
    x = coordinates.split(',')
    url = 'http://api.openweathermap.org/data/2.5/weather?lat=' + x[0] + '&lon=' + x[
        1] + '&APPID=6697b63dea7aa12280afbb7087640af5'
    response = urlopen(url)
    data = json.load(response)
    code = data['weather'][0]['id']
    main = data['weather'][0]['main']
    temp = data['main']['temp']
    temp2c = pytemperature.k2c(temp)
    country = data['sys']['country']
    city_name = data['name']
    template = 'weather.html'
    icons = json.loads(open(os.path.join(BASE_DIR, '../static/icons.json')).read())
    icon = icons[str(code)]['icon']
    description = icons[str(code)]['description_es']
    main_es = gs.translate(str(main), 'es')
    context = {
        'main': main_es,
        'temp': int(temp2c),
        'country': country,
        'city_name': city_name,
        'icon': icon,
        'description': description
    }
    return render(request, template, context)
