"""
This module fetch the data from openweather
api.
"""

import requests

from access_key import _fetch_api_key

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def build_url(city: list, imperial=False) -> str:
    """
    This build the url to use base on the following parameter.
    :param city:
    :param imperial:
    :return:
    """
    city_name: str = "+".join(city) if len(city) > 1 else "".join(city)
    api_key: str = f"{_fetch_api_key()}"
    units: str = "metric" if imperial else "imperial"
    url: str = f"{BASE_URL}?q={city_name}&units={units}&appid={api_key}"

    return url


def fetch_weather_data(url: str) -> dict:
    """
    This fetch the using the url build.
    :param url:
    :return:
    """
    query = requests.get(url)
    return query.json()
