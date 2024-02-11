import requests
import geocoder
import time
import datetime

class WeatherFetcher():    
    rained = False

    # Find timestamp and format into usable string for get request
    def timeThreeDaysAgo(self):
        # Get today's time in seconds since epoch and subtract 3 days. Format to usable string for API call
        t = time.time()
        t -= 259200
        t = datetime.datetime.fromtimestamp(t).strftime("%Y-%m-%dT%I:%M:%SZ")
        
        return t

    # Function to send GET request to weather open API. 
    def FetchWeather(self):
        # Grab user's approximate coordinates/location
        g = geocoder.ip('me')

        try:
            response = requests.get(f"https://api.weather.gov/points/{str(g.lat)},{str(g.lng)}")
        except:
            print("An exception has occured.")

        return response

    def CheckRainLastTwoObservations(self):
        response = self.FetchWeather()

        t = self.timeThreeDaysAgo()

        try:
            response = requests.get(f"https://api.weather.gov/stations/{response.json()['properties']['radarStation']}/observations?start={t}&limit=2")
            
            # Store decoded json into variable and store 'features' dict in weather
            data = response.json()          # Assign response json data
            weather = data['features']      # nested dict within data
            i = 0                           # Loop variable

            while (i < len(weather)):
                if 'Rain' in weather[i]['properties']['textDescription']:
                    self.rained = True
                i+=1

        except:
            print('An exception has occured.')

    def CheckRainLastThreeDays(self):
        response = self.FetchWeather()
        
        t = self.timeThreeDaysAgo()

        try:
            response = requests.get(f"https://api.weather.gov/stations/{response.json()['properties']['radarStation']}/observations?start={t}")
            
            # Store decoded json into variable and store 'features' dict in weather
            data = response.json()
            weather = data['features']
            i = 0 # Loop variable

            while (i < len(weather)):
                if 'Rain' in weather[i]['properties']['textDescription']:
                    self.rained = True
                i+=1

        except:
            print('An exception has occured.')

        return self.rained
    
    def FetchLastDateRained(self):
        response = self.FetchWeather()
        
        t = self.timeThreeDaysAgo()

        try:
            response = requests.get(f"https://api.weather.gov/stations/{response.json()['properties']['radarStation']}/observations?start={t}")
            
            # Store decoded json into variable and store 'features' dict in weather
            data = response.json()
            weather = data['features']
            i = 0 # Loop variable

            # Loop through weather observations, starting with latest date
            while (i < len(weather)):
                if 'Rain' in weather[i]['properties']['textDescription']:
                    self.rained = True
                    print('Latest rain date: ' + weather[i]['properties']['timestamp'])
                    break
                i+=1

        except:
            print('An exception has occured.')

        return self.rained
