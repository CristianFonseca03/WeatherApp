#Django
from django.shortcuts import render, redirect

#Python
from urllib.request import urlopen
import json
import pytemperature
from translate import Translator

def start_view(request):
    """Start View."""
    if request.method == 'POST':
        lat = request.POST['lat']
        lon = request.POST['lon']
        if lat == '0' or lon == '0':
             return render(request,'home.html',{'error':'Seleccione una cuidad'})
        return redirect('weather', coordinates = lat+','+lon)
    return render(request, 'home.html')

def weather(request,coordinates):
    translator = Translator(to_lang="Spanish")
    x=coordinates.split(',')
    url = 'http://api.openweathermap.org/data/2.5/weather?lat='+x[0]+'&lon='+x[1]+'&APPID=6697b63dea7aa12280afbb7087640af5'
    response = urlopen(url)
    data = json.load(response)
    main = data['weather'][0]['main']
    main_es = translator.translate(main)
    description = data['weather'][0]['description']
    description_es = translator.translate(description)
    description_es = description_es.replace('weather condition','')
    icon = 'http://openweathermap.org/img/w/'+data['weather'][0]['icon']+'.png'
    temp = data['main']['temp']
    temp2c = pytemperature.k2c(temp)
    country = data['sys']['country']
    city_name = data['name']
    template = 'weather.html'
    context = {
        'main': main_es,
        'description':description_es,
        'icon':icon,
        'temp':int(temp2c),
        'country':country,
        'city_name':city_name,
    }
    return render(request,template,context)
