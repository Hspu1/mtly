from enum import Enum, unique

from colorama import Fore


@unique
class Colors(Enum):
    GREEN = Fore.GREEN
    DARK_GREEN = Fore.LIGHTGREEN_EX
    LIGHT_BLUE = Fore.BLUE
    BLUE = Fore.LIGHTCYAN_EX
    DARK_BLUE = Fore.LIGHTBLUE_EX
    YELLOW = Fore.LIGHTYELLOW_EX
    ORANGE = Fore.YELLOW
    RED = Fore.LIGHTRED_EX
    PINK = Fore.LIGHTMAGENTA_EX
    DARK_PINK = Fore.RED
    PURPLE = Fore.MAGENTA
    DARK_PURPLE = Fore.WHITE
    GREY = Fore.LIGHTBLACK_EX
    BLACK = Fore.BLACK
    WHITE = Fore.RESET
