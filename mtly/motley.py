from mtly.motley_settings import (
    Colors, ColorCombos, Styles, matching_color_combo, selecting
)


def motley(text: str,
           color: Colors = Colors.WHITE,
           color_combo: ColorCombos = Colors.WHITE,
           style: Styles = Styles.DEFAULT) -> str:
    if color_combo == Colors.WHITE:
        return style.value + color.value + text + "\x1B[0m"

    if color == Colors.WHITE:
        return matching_color_combo(
            entered_text=text, entered_style=style,
            entered_color_combo=color_combo
        )

    return selecting(
        entered_style=style, entered_color=color,
        entered_color_combo=color_combo
    )
