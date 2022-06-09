import json,urllib
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
key="5dc8a7c85f444a8998e143150220806"
# Create your views here.
def weather(request):
    try:
        if request.method == 'POST': 
            city = request.POST['city'] 
        # url="http://api.weatherapi.com/v1/current.json?key=5dc8a7c85f444a8998e143150220806&q="+city+"&aqi=no"
        # current location  url
            source = urllib.request.urlopen( 
                'http://api.weatherapi.com/v1/current.json?key='+key+'&q='+city+'&aqi=no').read() 
        
            list_of_data = json.loads(source) 
            CurrentAPI = {
            "Town ":str(list_of_data['location']['name']),
                "State ": str(list_of_data['location']['region']),
                "country ": str(list_of_data['location']['country']),
                "latitude ":str(list_of_data['location']['lat']), 
                "Longitude ": str(list_of_data['location']['lon']), 
                "Time Zone ": str(list_of_data['location']['tz_id']),
                "Local Time ": str(list_of_data['location']['localtime_epoch']),
                "Time ": str(list_of_data['location']['localtime']),
            } 
            # forecast URl
            source2 = urllib.request.urlopen( 
                'http://api.weatherapi.com/v1/forecast.json?key='+key+'&q='+city+'&days=1&aqi=no&alerts=no').read() 
            list_of_data1 = json.loads(source2) 
            ForeCastAPI={
                "Down ":str(list_of_data1['forecast']['forecastday'][0]['astro']['sunrise']),
                "Dusk ":str(list_of_data1['forecast']['forecastday'][0]['astro']['sunset']),
                "moon Lit ":str(list_of_data1['forecast']['forecastday'][0]['astro']['moonrise']),
                "Moon Sleep ":str(list_of_data1['forecast']['forecastday'][0]['astro']['moonset']),
                    "Orientation ":str(list_of_data1['forecast']['forecastday'][0]['astro']['moon_phase']),
                    "Illumination ":str(list_of_data1['forecast']['forecastday'][0]['astro']['moon_illumination']),
                }
        else:
            CurrentAPI ={} 
            ForeCastAPI={}
            return render(request, "weather.html", CurrentAPI) 
        return HttpResponse(f"<h1>Location</h1><br><h3>{CurrentAPI}<h3> <br><h1>ForeCast Astro</h1><br><h3>{ForeCastAPI}</h3>")
    except:
        return HttpResponse(f"<h1>{city} no found</h1>")