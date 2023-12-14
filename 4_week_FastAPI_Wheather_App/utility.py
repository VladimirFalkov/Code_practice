import requests
from environs import Env

env = Env()
env.read_env()


def get_lat_lon(country_code: str, city_name: str):
    access_key = env("SECRET_API_KEYS_FOR_WEATHER")
    limit = 5
    api_result = requests.get(
        f"http://api.openweathermap.org/geo/1.0/direct?q={city_name},{country_code}&limit={limit}&appid={access_key}"
    )
    api_response = api_result.json()

    lon = api_response[0]["lon"]
    lat = api_response[0]["lat"]
    return lat, lon


def get_weather(ip):
    country_code, city_name = get_location(ip)
    print(country_code, city_name)
    access_key = env("SECRET_API_KEYS_FOR_WEATHER")
    api_result = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={country_code},{city_name}&units=metric&appid={access_key}"
    )

    api_response = api_result.json()
    return api_response["main"]


def get_location(ip: str):
    response = requests.get(f"http://ip-api.com/json/{ip}?lang=ru")
    if response.status_code == 404:
        print("Oops")
    result = response.json()
    if result["status"] == "fail":
        return ("Москва", "RU")

    return result["city"], result["countryCode"]
