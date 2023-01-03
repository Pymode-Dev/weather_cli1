from access_key import _get_api_key
import requests

BASE_WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"


def build_url(city: list, imperial=False) -> str:
    """
    This build the api url base on user's input.
    """
    api_key: str = _get_api_key()
    city_name: str = "+".join(city) if len(city) > 1 else "".join(city)
    unit: str = "metric" if imperial else "imperial"
    url: str = f"{BASE_WEATHER_API_URL}?q={city_name}&units={unit}" \
               f"&appid={api_key}"
    return url


def fetch_weather_data(url: str) -> dict:
    """
    This fetch the weather data.
    """
    data = requests.get(url)
    return data.json()
