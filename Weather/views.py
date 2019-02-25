# Django
from django.shortcuts import render, redirect
from Weather.settings.base import BASE_DIR

# Python
from urllib.request import urlopen
import json
import pytemperature
import os
import datetime


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


def get_day(day):
    now = datetime.datetime.today()
    one_day = datetime.timedelta(days=1)
    two_day = datetime.timedelta(days=2)
    three_day = datetime.timedelta(days=3)
    if day == 0:
        return now
    if day == -1:
        return now + one_day
    if day == -2:
        return now + two_day
    if day == -3:
        return now + three_day


def weather(request, coordinates):
    x = coordinates.split(',')
    url = 'http://api.openweathermap.org/data/2.5/weather?lat=' + x[0] + '&lon=' + x[
        1] + '&units=metric&APPID=6697b63dea7aa12280afbb7087640af5'
    response = urlopen(url)
    data = json.load(response)
    url = 'https://api.openweathermap.org/data/2.5/forecast?lat=' + x[0] + '&lon=' + x[
        1] + '&units=metric&APPID=6697b63dea7aa12280afbb7087640af5'
    response = urlopen(url)
    past_data = json.load(response)
    code = data['weather'][0]['id']
    main = data['weather'][0]['main']
    temp = data['main']['temp']
    icon_code = data['weather'][0]["icon"]
    try:
        country = data['sys']['country']
    except KeyError:
        country = "NN"
    city_name = data['name']
    template = 'weather.html'
    icons = json.loads(open(os.path.join(BASE_DIR, '../static/icons.json')).read())
    dates = json.loads(open(os.path.join(BASE_DIR, '../static/date.json')).read())
    if get_day_status(icon_code):
        status = "night"
        icon = icons[str(code)]['icon_night']
    else:
        icon = icons[str(code)]['icon_day']
        status = "day"
    description = icons[str(code)]['description_es']
    try:
        main_es = icons["descriptions"][main]
    except KeyError:
        main_es = main
    """day 1"""
    main_1 = past_data["list"][6]["weather"][0]["main"]
    code_1 = past_data["list"][6]["weather"][0]["id"]
    icon_1 = past_data["list"][6]["weather"][0]["icon"]
    if get_day_status(icon_1):
        icon_1 = icons[str(code_1)]['icon_night']
    else:
        icon_1 = icons[str(code_1)]['icon_day']
    try:
        main_es_1 = icons["descriptions"][main_1]
    except KeyError:
        main_es_1 = main
    """day 2"""
    main_2 = past_data["list"][14]["weather"][0]["main"]
    code_2 = past_data["list"][14]["weather"][0]["id"]
    icon_2 = past_data["list"][14]["weather"][0]["icon"]
    if get_day_status(icon_2):
        icon_2 = icons[str(code_2)]['icon_night']
    else:
        icon_2 = icons[str(code_2)]['icon_day']
    try:
        main_es_2 = icons["descriptions"][main_2]
    except KeyError:
        main_es_2 = main
    """day 3"""
    main_3 = past_data["list"][22]["weather"][0]["main"]
    code_3 = past_data["list"][22]["weather"][0]["id"]
    icon_3 = past_data["list"][22]["weather"][0]["icon"]
    if get_day_status(icon_3):
        icon_3 = icons[str(code_3)]['icon_night']
    else:
        icon_3 = icons[str(code_3)]['icon_day']
    try:
        main_es_3 = icons["descriptions"][main_3]
    except KeyError:
        main_es_3 = main
    context = {
        'main': main_es,
        'temp': temp,
        'country': country,
        'city_name': city_name,
        'icon': icon,
        'description': description,
        'status': status,
        'month': dates["mouths"][str(get_day(0).month)],
        'today': get_day(0).day,
        'day_': dates["days"][get_day(0).strftime('%A').upper()],
        'past_climate': {
            '1': {
                'day': get_day(-1).day,
                'month': dates["mouths"][str(get_day(-1).month)],
                'day_': dates["days"][get_day(-1).strftime('%A').upper()],
                'temp':past_data["list"][6]["main"]["temp"],
                'icon':icon_1,
                'main':main_es_1
            },
            '2': {
                'day': get_day(-2).day,
                'month': dates["mouths"][str(get_day(-2).month)],
                'day_': dates["days"][get_day(-2).strftime('%A').upper()],
                'temp':past_data["list"][14]["main"]["temp"],
                'icon':icon_2,
                'main':main_es_2
            },
            '3': {
                'day': get_day(-3).day,
                'month': dates["mouths"][str(get_day(-3).month)],
                'day_': dates["days"][get_day(-3).strftime('%A').upper()],
                'temp':past_data["list"][22]["main"]["temp"],
                'icon':icon_3,
                'main':main_es_3
            },
        }
    }
    return render(request, template, context)
