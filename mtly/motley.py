import logging

from colorama import Fore, Style

from mtly.color_combos import (
    volcano_color_combo, fresh_color_combo, night_color_combo
)
from mtly.logging_settings import lg


def motley(text: str,
           color: str = "default",
           style: str = "default",
           color_combo: str = "default") -> str:
    color, style, color_combo = (
        color.lower(), style.lower(), color_combo.lower()
    )
    if lg.isEnabledFor(logging.INFO):
        lg.info(f"text={repr(text)}, "
                f"color={repr(color)}, "
                f"style={repr(style)}, "
                f"color_combo={repr(color_combo)}"
        )

    colors = {
        "green": Fore.GREEN, "dark_green": Fore.LIGHTGREEN_EX,
        "light_blue": Fore.BLUE, "blue": Fore.LIGHTCYAN_EX,
        "dark_blue": Fore.LIGHTBLUE_EX,
        "yellow": Fore.LIGHTYELLOW_EX, "orange": Fore.YELLOW,
        "pink": Fore.LIGHTMAGENTA_EX, "dark_pink": Fore.RED,
        "red": Fore.LIGHTRED_EX,
        "purple": Fore.MAGENTA, "dark_purple": Fore.WHITE,
        "grey": Fore.LIGHTBLACK_EX, "black": Fore.BLACK,
        "default": Fore.RESET
    }
    styles = {
        "bold": Style.BRIGHT, "italic": f"\x1B[3m{text}\x1B[0m",
        "bold_italic": f"\x1B[3m{Style.BRIGHT + text}\x1B[0m",
        "default": Style.NORMAL
    }
    color_combos = {
        "volcano": volcano_color_combo(entered_text=text, entered_style=style),
        "fresh": fresh_color_combo(entered_text=text, entered_style=style),
        "night": night_color_combo(entered_text=text, entered_style=style),
        "default": Fore.RESET
    }

    try:
        colors[color], styles[style], color_combos[color_combo]
    except KeyError as ker:
        if lg.isEnabledFor(logging.ERROR):
            lg.error("Был указан неверный "
                     "цвет и/или стиль и/или цветовую комбинация: "
                     f"{ker}", exc_info=ker
            )

        return ("Вы указали неверный "
                "цвет и/или стиль и/или цветовую комбинацию. "
                "Вы можете узнать о существующих перейдя по ссылке: "
                "https://github.com/Hspu1/motley"
        )

    else:
        if color_combo == "default":
            return f"{colors[color]}{styles[style]}{text}" \
                if style in ("bold", "default") \
                else f"{colors[color]}{styles[style]}"

        return color_combos[color_combo]
