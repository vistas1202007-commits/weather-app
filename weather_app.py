# ============================================================
# Project  : Weather App - Real-time Weather Fetcher
# Author   : Shivani Sharma
# Language : Python
# API      : OpenWeatherMap (Free API)
# ============================================================

import requests  # To make HTTP requests to weather API

# ---------------------------------------------------------------
# API Configuration
# Get your FREE API key from: https://openweathermap.org/api
# Replace the value below with your actual API key
# ---------------------------------------------------------------
API_KEY = "your_api_key_here"  # <-- Replace with your API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city_name):
    """
    Fetch weather data for a given city using OpenWeatherMap API.
    
    Parameters:
        city_name : Name of the city (string)
    
    Returns:
        Dictionary with weather data, or None if error occurs
    """
    # Build the request parameters
    params = {
        "q": city_name,         # City name
        "appid": API_KEY,       # API key for authentication
        "units": "metric"       # metric = Celsius, imperial = Fahrenheit
    }

    try:
        # Send GET request to the API
        response = requests.get(BASE_URL, params=params)

        # Check if request was successful (status code 200 = OK)
        if response.status_code == 200:
            return response.json()  # Return JSON data as dictionary

        elif response.status_code == 404:
            print(f"❌ City '{city_name}' not found. Please check the spelling.")
            return None

        elif response.status_code == 401:
            print("❌ Invalid API Key. Please check your API key.")
            return None

        else:
            print(f"❌ Error: {response.status_code}")
            return None

    except requests.exceptions.ConnectionError:
        # Handles no internet connection
        print("❌ No internet connection. Please check your network.")
        return None


def display_weather(data, city_name):
    """
    Display weather information in a clean, readable format.
    
    Parameters:
        data      : Weather data dictionary from API
        city_name : Name of the city (string)
    """
    # Extract required values from the API response
    temperature  = data["main"]["temp"]         # Current temperature
    feels_like   = data["main"]["feels_like"]   # Feels like temperature
    humidity     = data["main"]["humidity"]      # Humidity percentage
    description  = data["weather"][0]["description"]  # Weather description
    wind_speed   = data["wind"]["speed"]         # Wind speed in m/s
    country      = data["sys"]["country"]        # Country code

    # Display formatted weather report
    print("\n" + "=" * 45)
    print(f"  🌍 Weather Report: {city_name.title()}, {country}")
    print("=" * 45)
    print(f"  🌡️  Temperature   : {temperature}°C")
    print(f"  🤔 Feels Like    : {feels_like}°C")
    print(f"  💧 Humidity      : {humidity}%")
    print(f"  🌬️  Wind Speed    : {wind_speed} m/s")
    print(f"  ☁️  Condition     : {description.capitalize()}")
    print("=" * 45)


def main():
    """
    Main function - runs the Weather Application.
    Allows user to check weather for multiple cities.
    """
    print("=" * 45)
    print("     🌤️  WEATHER APP - Real-time Weather")
    print("=" * 45)

    while True:
        print("\nOptions:")
        print("  1. Check Weather")
        print("  2. Exit")

        choice = input("\nEnter your choice (1/2): ").strip()

        if choice == '1':
            city = input("Enter city name: ").strip()
            if city == "":
                print("⚠️  City name cannot be empty!")
                continue

            # Fetch and display weather
            weather_data = get_weather(city)
            if weather_data:
                display_weather(weather_data, city)

        elif choice == '2':
            print("\n👋 Goodbye! Stay weather-aware!")
            break

        else:
            print("❌ Invalid choice! Please enter 1 or 2.")


# Entry point
if __name__ == "__main__":
    main()
