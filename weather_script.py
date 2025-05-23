# Fetch weather data from OpenWeatherMap API

import requests

def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data.get('main', {})
        weather = data.get('weather', [{}])[0]
        temp = main.get('temp')
        humidity = main.get('humidity')
        description = weather.get('description')
        print(f"Weather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description}")
    else:
        print(f"Failed to get weather data for {city}. Error: {response.status_code}")

def main():
    api_key = input("Enter your OpenWeatherMap API key: ")
    while True:
        city = input("Enter city name (or 'exit' to quit): ")
        if city.lower() == 'exit':
            print("Exiting weather app.")
            break
        get_weather(city, api_key)

if __name__ == "__main__":
    main()
