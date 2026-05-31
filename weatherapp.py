import requests

API_KEY = "your_api_key_here"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    
    response = requests.get(BASE_URL, params=params)
    
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        print("City not found!")
        return None
    elif response.status_code == 401:
        print("Wrong API key!")
        return None
    else:
        print("Something went wrong!")
        return None

def show_weather(data, city):
    temp = data["main"]["temp"]
    feels = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    condition = data["weather"][0]["description"]
    country = data["sys"]["country"]
    
    print("\n----------------------------------")
    print(f"  Weather in {city.title()}, {country}")
    print("----------------------------------")
    print(f"  Temperature : {temp}°C")
    print(f"  Feels Like  : {feels}°C")
    print(f"  Humidity    : {humidity}%")
    print(f"  Wind Speed  : {wind} m/s")
    print(f"  Condition   : {condition}")
    print("----------------------------------")

print("--- Weather App ---")

while True:
    print("\n1. Check Weather")
    print("2. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        city = input("Enter city name: ")
        data = get_weather(city)
        if data:
            show_weather(data, city)
            
    elif choice == "2":
        print("Bye!")
        break
    else:
        print("Invalid choice!")
