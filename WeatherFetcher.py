import requests
import json
import geocoder

class WeatherFetcher:
    
    
    
    def FetchWeather(self):
        g = geocoder.ip('me')
        # coordinates = {
        #     "lat": str(g.lat),
        #     "lng": str(g.lng)
        # }

        try:
            g
            #response = requests.get("https://api.weather.gov/openapi.json")
            response = requests.get(f"https://api.weather.gov/points/{str(g.lat)},{str(g.lng)}")
            response = requests.get(response.json()['properties']['forecast'])
            text = json.dumps(response.json(), sort_keys=True, indent=3)
            print(text)
        except:
            print('An exception has occured.')


weather = WeatherFetcher()

weather.FetchWeather()