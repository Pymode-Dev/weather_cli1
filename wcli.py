import argparse
from weather import build_url, fetch_weather_data
from terminal_modifier import RESET, REVERSE, change_color, _render_emoji


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch weather condition of your city.",
        prog="wcli",
        epilog="Thanks for using Weather CLI.",
        add_help=True,
    )
    parser.add_argument("city", help="Enter city", nargs="+",)
    parser.add_argument("-i", "--imperial", action="store_true", help="To display temperature in Celsius")

    return parser.parse_args()


def display_weather_info():
    args = parse_arguments()
    weather_data: dict = fetch_weather_data(build_url(args.city, args.imperial))

    city: str = weather_data["name"]
    temperature: str = weather_data["main"]["temp"]
    description = weather_data["weather"][0]["description"]
    units: str = "C" if args.imperial else "F"
    weather_id: int = weather_data["weather"][0]["id"]

    print(f"{REVERSE}{city:^20}{REVERSE}", end="")
    print(f"{RESET}", end="")
    symbol, color = _render_emoji(weather_id)
    print(f"\t{symbol}", end="")
    change_color(color)
    print(f"{description.capitalize()}", end=" ")
    print(f"{RESET}", end="")
    print(f"({temperature}`{units})")


def main():
    display_weather_info()


if __name__ == '__main__':
    main()
