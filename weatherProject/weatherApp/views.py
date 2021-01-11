import urllib.request
import json
from django.shortcuts import render


def index(request):
    try:

        if request.method == 'POST':
            city = request.POST['city']

            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' +
                                            city + '&units=metric&appid=83268b6343df9182f622b2b137f0ec14').read()
            list_of_data = json.loads(source)

            data = {
                "city": city,
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ','
                + str(list_of_data['coord']['lat']),
                "temp": str(list_of_data['main']['temp']) + '°C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                "main": str(list_of_data['weather'][0]['main']),
                "description": str(list_of_data['weather'][0]['description']),
                "icon": list_of_data['weather'][0]['icon'],
            }
            print(data)
        else:
            data = {}

    except urllib.error.HTTPError as exception:
        #     # print('ddddddd', exception)
        return render(request, 'weatherApp/index.html', {'error': "City does not exist."})

    return render(request, "weatherApp/index.html", data)
