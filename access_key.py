"""
Fetch api key from configuration file.
"""

from configparser import ConfigParser


def _fetch_api_key() -> str:
    """
    Fetch api key from configuration file.
    """
    try:
        configuration = ConfigParser()
        configuration.read("secrets.ini")
        return configuration["openweather"]["apikey"]
    except ValueError:
        print("Invalid filename or check your config file")
