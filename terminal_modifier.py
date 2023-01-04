ITALICIZE = "\033[;3m"
REVERSE = "\033[;7m"
RESET = "\033[0m"
PADDING = 20

RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
YELLOW = "\033[33m"
WHITE = "\033[37m"


def change_color(color: str):
    print(color, end="")


def change_font():
    print(ITALICIZE, end="")


def handle_color(weather_id: int) -> str:
    if weather_id in range(200, 300):
        render = RED
    elif weather_id in range(300, 400):
        render = BLUE
    elif weather_id in range(400, 500):
        render = CYAN
    elif weather_id in range(500, 600):
        render = GREEN
    elif weather_id in range(600, 700):
        render = YELLOW
    elif weather_id in range(700, 800):
        render = WHITE
    else:
        render = RESET
    return render
