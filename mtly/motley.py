import logging


from mtly.logging_settings import lg
from mtly.motley_settings import (
    Colors, ColorCombos, Styles, volcano, fresh, night
)


def motley(text: str,
           color: Colors = Colors.WHITE,
           color_combo: ColorCombos = Colors.WHITE,
           style: Styles = Styles.DEFAULT):
    if lg.isEnabledFor(logging.INFO):
        lg.info(f"text={repr(text)}, "
                f"color={repr(color)}, "
                f"color_combo={repr(color_combo)}, "
                f"style={repr(style)}"
        )

    if color_combo == Colors.WHITE:
        return style.value + color.value + text + "\x1B[0m"

    if color == Colors.WHITE:
        match color_combo:
            case ColorCombos.VOLCANO:
                return style.value + volcano(entered_text=text)
            case ColorCombos.FRESH:
                return style.value + fresh(entered_text=text)
            case ColorCombos.NIGHT:
                return style.value + night(entered_text=text)
            case _:
                return style.value + text

    return style.value + (f"Вы указали сразу и {color.value + 'цвет'}"
                          f"{color.WHITE.value + ', и'} "
            f"{volcano("цветовую комбинацию") 
                if '.' not in f'{color_combo}'[-7:].lower() 
                else fresh("цветовую комбинацию") 
                    if f'{color_combo}'[-5:].lower() == "fresh" 
                    else night("цветовую комбинацию")}")
