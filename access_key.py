from configparser import ConfigParser


def _get_api_key() -> str:
    """
    Fetch API key from config file.
    """
    configuration = ConfigParser()
    configuration.read("secrets.ini")
    return configuration["openweather"]["api_key"]
