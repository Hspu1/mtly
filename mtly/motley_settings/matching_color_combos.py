from mtly.motley_settings import (
    ColorCombos, Styles, volcano, fresh, night
)


def matching_color_combo(
        entered_color_combo: ColorCombos,
        entered_style: Styles,
        entered_text: str) -> str:
    match entered_color_combo:
        case ColorCombos.VOLCANO:
            return entered_style.value + volcano(entered_text=entered_text)
        case ColorCombos.FRESH:
            return entered_style.value + fresh(entered_text=entered_text)
        case ColorCombos.NIGHT:
            return entered_style.value + night(entered_text=entered_text)
        case _:
            return entered_style.value + entered_text
