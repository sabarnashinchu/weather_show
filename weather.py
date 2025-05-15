from colorama import Fore, Style, init
from datetime import datetime
import random

# Initialize colorama
init()

# Predefined weather patterns
WEATHER_PATTERNS = {
    'Sunny': {
        'temp_range': (20, 30),
        'humidity_range': (30, 50),
        'wind_range': (0, 10),
        'description': 'Clear sunny skies'
    },
    'Cloudy': {
        'temp_range': (15, 25),
        'humidity_range': (50, 70),
        'wind_range': (5, 15),
        'description': 'Partly cloudy'
    },
    'Rainy': {
        'temp_range': (10, 20),
        'humidity_range': (70, 90),
        'wind_range': (10, 20),
        'description': 'Light rain'
    },
    'Stormy': {
        'temp_range': (8, 15),
        'humidity_range': (80, 95),
        'wind_range': (20, 30),
        'description': 'Thunder storms'
    }
}

def generate_weather_data(city):
    # Randomly select a weather pattern
    weather_type = random.choice(list(WEATHER_PATTERNS.keys()))
    pattern = WEATHER_PATTERNS[weather_type]
    
    # Generate random values within the pattern's ranges
    temp = round(random.uniform(*pattern['temp_range']), 1)
    feels_like = round(temp + random.uniform(-2, 2), 1)
    humidity = round(random.uniform(*pattern['humidity_range']))
    wind_speed = round(random.uniform(*pattern['wind_range']), 1)
    
    # Generate sunrise and sunset times
    base_sunrise = datetime.now().replace(hour=6, minute=0)
    base_sunset = datetime.now().replace(hour=18, minute=0)
    sunrise_offset = random.randint(-30, 30)
    sunset_offset = random.randint(-30, 30)
    
    return {
        'city': city,
        'temp': temp,
        'feels_like': feels_like,
        'humidity': humidity,
        'wind_speed': wind_speed,
        'description': pattern['description'],
        'sunrise': (base_sunrise.hour * 60 + base_sunrise.minute + sunrise_offset) // 60,
        'sunrise_mins': (base_sunrise.hour * 60 + base_sunrise.minute + sunrise_offset) % 60,
        'sunset': (base_sunset.hour * 60 + base_sunset.minute + sunset_offset) // 60,
        'sunset_mins': (base_sunset.hour * 60 + base_sunset.minute + sunset_offset) % 60
    }

def display_weather(weather_data):
    print(f"\n{Fore.CYAN}Weather in {weather_data['city']}{Style.RESET_ALL}")
    print("=" * 40)
    print(f"{Fore.YELLOW}Temperature: {Fore.WHITE}{weather_data['temp']}°C")
    print(f"{Fore.YELLOW}Feels like: {Fore.WHITE}{weather_data['feels_like']}°C")
    print(f"{Fore.YELLOW}Conditions: {Fore.WHITE}{weather_data['description']}")
    print(f"{Fore.YELLOW}Humidity: {Fore.WHITE}{weather_data['humidity']}%")
    print(f"{Fore.YELLOW}Wind Speed: {Fore.WHITE}{weather_data['wind_speed']} m/s")
    print(f"{Fore.YELLOW}Sunrise: {Fore.WHITE}{weather_data['sunrise']:02d}:{weather_data['sunrise_mins']:02d}")
    print(f"{Fore.YELLOW}Sunset: {Fore.WHITE}{weather_data['sunset']:02d}:{weather_data['sunset_mins']:02d}")
    print("=" * 40)

def main():
    print(f"{Fore.CYAN}Welcome to Weather Show! (Simulation Mode){Style.RESET_ALL}")
    print(f"{Fore.GREEN}This is a demo version that generates simulated weather data.{Style.RESET_ALL}")
    
    while True:
        city = input(f"\n{Fore.GREEN}Enter city name (or 'quit' to exit): {Style.RESET_ALL}")
        if city.lower() == 'quit':
            print(f"\n{Fore.CYAN}Thank you for using Weather Show! Goodbye!{Style.RESET_ALL}")
            break
            
        weather_data = generate_weather_data(city)
        display_weather(weather_data)

if __name__ == "__main__":
    main() 