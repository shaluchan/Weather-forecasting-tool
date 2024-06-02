from colorama import init, Fore, Back, Style
init()
import pandas as pd
import requests
def main():
    print(Fore.YELLOW + Back.BLUE+"welcome to the weather tool:"+Style.RESET_ALL)
    print(Fore.YELLOW + Back.BLUE+"type 'exit'to quit the bot:"+Style.RESET_ALL)
    api_key = '3f9950f17f2e8ba67391b5d212d7c2c9'
   
    while True:
      city_name=input(Fore.YELLOW+"enter a city name to find the weather:"+Style.RESET_ALL)
      if city_name.lower() == 'exit':
            print("\nGoodbye!hope to see u next tym")
            break
    
      data = get_weather_data(city_name, api_key)
      display_weather(data)#function calling

    
def get_weather_data(city_name,api_key):
    api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
    response = requests.get(api_url)
    data = response.json()
    return data

def display_weather(data):
    if data.get('cod') != 200:
        print(f"Error fetching data: {data.get('message', '-_- \nUnknown error')}")
        return

    location = data.get('name', 'Unknown location')
    weather = data.get('weather', [{}])[0].get('description', 'No description available')
    temp = data.get('main', {}).get('temp', 'No temperature data')
    feels_like = data.get('main', {}).get('feels_like', 'No feels like data')
    humidity = data.get('main', {}).get('humidity', 'No humidity data')
    wind_speed = data.get('wind', {}).get('speed', 'No wind speed data')

    print(Style.BRIGHT+f"Weather in {location}:"+Style.RESET_ALL)
    print(Fore.CYAN+f"Description: {weather}"+Style.RESET_ALL)
    print(Fore.YELLOW+f"Temperature: {temp}°C"+Style.RESET_ALL)
    print(Fore.MAGENTA+f"Feels like: {feels_like}°C"+Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX+f"Humidity: {humidity}%"+Style.RESET_ALL)
    print(Fore.GREEN+f"Wind speed: {wind_speed} m/s"+Style.RESET_ALL)
    print("\n")

if __name__ == "__main__":
    main()
