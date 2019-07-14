import requests, json
from datetime import datetime

# Enter your API key here
api_key = ""
# base_url variable to store url
base_url = "http://api.openweathermap.org/data/2.5/weather?"

print("Enter your zip code")
zip= input()
complete_url = base_url + "zip=" + str(zip) + ",us&appid="+api_key

response = requests.get(complete_url)

x = response.json()

if x["cod"] != "404":

    y = x["main"]
    Name=x["name"]
    wind_speed = x["wind"]["speed"]
    wind_direc=x["wind"]["deg"]
    current_temperature = y["temp"]
    current_pressure = y["pressure"]
    timereport = datetime.now()


    # print following values
    print(" Name = "+Name+
        " Current Temperature (in kelvin unit) = " +
          str(current_temperature) +
          "\n atmospheric pressure (in hPa unit) = " +
          str(current_pressure) +
          "\n Wind speed = " +
          str(wind_speed)+
          "\n Wind Direction = "+
          str(wind_direc)+
          "\n Time = "+
          str(timereport) )

else:
    print(" City Not Found ")
