import requests
from datetime import datetime  # to convert unix time to datetime format

# API key from OpenWeather
APIkey = '110ba51a619d128148d52e80a46e58dd'

# Greeting
print('Welcome to the weather tracker!')
city_input = input('Enter city: ')
#print(city_input) #check if city input is working 

#This will use the request library to get the URL to get the weather data
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&units=imperial&APPID={APIkey}"
)

data = weather_data.json()

# Check if city was found
if int(weather_data.json().get('cod')) == 404:
    print('No City Found')
else:
    #print(weather_data.status_code) #check if weather code is working, if output is 200, were good to go
    #print(weather_data.json()) #Check if we get weather data
    weather_main = data['weather'][0]['main']
    weather_desc = data['weather'][0]['description'].title()
    temp = round(data['main']['temp'])
    feels_like = round(data['main']['feels_like'])
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']

    # Sunrise & Sunset (convert from Unix)
    sunrise = datetime.fromtimestamp(data['sys']['sunrise']).strftime('%I:%M %p')
    sunset = datetime.fromtimestamp(data['sys']['sunset']).strftime('%I:%M %p')

    # Output
    print(f"\nWeather in {city_input}:")
    print("==============================")
    print(f"  Condition: {weather_main} ({weather_desc})")
    print(f"  Temperature: {temp}°F (Feels like {feels_like}°F)") # Shift+Option+8 for ° on Mac
    print(f"  Humidity: {humidity}%")
    print(f"  Wind Speed: {wind_speed} mph")
    print(f"  Sunrise: {sunrise}")
    print(f"  Sunset: {sunset}")
    print("==============================")