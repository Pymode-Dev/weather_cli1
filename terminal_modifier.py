PADDING = 20

REVERSE = "\033[;7m"
RESET = "\033[0m"
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
YELLOW = "\033[33m"
WHITE = "\033[37m"

THUNDERSTORM = range(200, 300)
DRIZZLE = range(300, 400)
RAIN = range(500, 600)
SNOW = range(600, 700)
ATMOSPHERE = range(700, 800)
CLEAR = range(800, 801)
CLOUDY = range(801, 900)


def change_color(color: str):
    print(color, end="")


def _render_emoji(weather_id: int):
    if weather_id in THUNDERSTORM:
        render = ("💥", RED)
    elif weather_id in DRIZZLE:
        render = ("💧", CYAN)
    elif weather_id in RAIN:
        render = ("💦", BLUE)
    elif weather_id in SNOW:
        render = ("☃", WHITE)
    elif weather_id in ATMOSPHERE:
        render = ("🌀", BLUE)
    elif weather_id in CLEAR:
        render = ("🔆", YELLOW)
    elif weather_id in CLOUDY:
        render = ("💨", WHITE)
    else:
        render = ("🌈", RESET)

    return render
