import requests
from environs import Env

env = Env()
env.read_env()


def fetch_weather(ip):
    country_code, city_name = get_location(ip)
    access_key = env("SECRET_API_KEYS_FOR_WEATHER")
    api_result = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={country_code},{city_name}&units=metric&appid={access_key}"
    )

    api_response = api_result.json()
    return api_response["main"]


import requests


import requests


def get_location(ip: str):
    url = f"http://ip-api.com/json/{ip}?lang=en"
    response = requests.get(url)

    if response.status_code == 404:
        return None

    result = response.json()
    if result.get("status") == "fail":
        return "Moscow", "RU"

    city = result["city"]
    country_code = result["countryCode"]
    return city, country_code
