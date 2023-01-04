import argparse

from terminal_modifier import (REVERSE, RESET,
                               change_color, change_font,
                               handle_color)
from weather import build_url, fetch_weather_data


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="wcli",
        description="Check your city temperature.",
        epilog="Thanks for using weather cli app.",
    )

    parser.add_argument("city", help="Enter the city name", nargs="+", type=str)
    parser.add_argument("-i", "--imperial", action="store_true", help="To display in Celsius or Fahrenheit.")

    return parser.parse_args()


def print_info():
    args = parse_args()
    url = build_url(args.city, args.imperial)
    weather_data = fetch_weather_data(url)

    city = weather_data["name"]
    country = weather_data["sys"]["country"]
    weather_description = weather_data["weather"][0]["description"]
    weather_id = weather_data["weather"][0]["id"]
    temperature = weather_data["main"]["temp"]
    units = "C" if args.imperial else "F"

    change_font()
    change_color(REVERSE)
    print(f"{city}, {country}.", end="")
    change_color(RESET)
    change_color(handle_color(weather_id))
    change_font()
    print(f"\t{weather_description.capitalize()}", end=" ")
    change_color(RESET)
    change_font()
    print(f"({temperature}`{units})")


def main():
    print_info()


if __name__ == '__main__':
    main()
