from colorama import Fore, Style


def pattern_color_combos(
        pattern_colors: tuple,
        pattern_text: str,
        pattern_style: str
) -> str:
    combo_colors = pattern_colors

    new_text = ""
    index = 0
    for item in pattern_text:
        try:
            combo_colors[index]
        except IndexError:
            index = 0
        else:
            new_text += combo_colors[index] + item
            index += 1

    local_pattern_styles = {
        "bold": Style.BRIGHT, "italic": f"\x1B[3m{new_text}\x1B[0m",
        "bold_italic": f"\x1B[3m{Style.BRIGHT + new_text}\x1B[0m",
        "default": Style.NORMAL
    }

    return local_pattern_styles[pattern_style] \
        if pattern_style in ("italic", "bold_italic") \
        else local_pattern_styles[pattern_style] + new_text


def volcano_color_combo(entered_text: str, entered_style: str):
    local_colors = (
        Fore.LIGHTRED_EX, Fore.BLACK, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX, Fore.RESET,
        Fore.LIGHTRED_EX, Fore.BLACK, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX, Fore.RESET,
        Fore.LIGHTRED_EX, Fore.BLACK, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX, Fore.RESET,
        Fore.LIGHTRED_EX, Fore.BLACK, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX, Fore.RESET,
        Fore.LIGHTRED_EX, Fore.BLACK, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX, Fore.RESET,
        Fore.LIGHTRED_EX, Fore.BLACK, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX, Fore.RESET,
        Fore.LIGHTRED_EX, Fore.BLACK, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX, Fore.RESET,
        Fore.LIGHTRED_EX, Fore.BLACK, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX, Fore.RESET,
        Fore.LIGHTRED_EX, Fore.BLACK, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX, Fore.RESET,
        Fore.LIGHTRED_EX, Fore.BLACK, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX, Fore.RESET,
        Fore.LIGHTRED_EX, Fore.BLACK, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX, Fore.RESET,
        Fore.LIGHTRED_EX, Fore.BLACK, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX, Fore.RESET,
        Fore.LIGHTRED_EX, Fore.BLACK, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX, Fore.RESET,
        Fore.LIGHTRED_EX, Fore.BLACK, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX, Fore.RESET,
        Fore.LIGHTRED_EX, Fore.BLACK, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX, Fore.RESET
    )

    return pattern_color_combos(
        pattern_colors=local_colors, pattern_text=entered_text,
        pattern_style=entered_style
    )


def fresh_color_combo(entered_text: str, entered_style: str):
    local_colors = (
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX,
        Fore.BLUE, Fore.LIGHTCYAN_EX, Fore.LIGHTBLUE_EX,
        Fore.GREEN, Fore.LIGHTGREEN_EX
    )

    return pattern_color_combos(
        pattern_colors=local_colors, pattern_text=entered_text,
        pattern_style=entered_style
    )


def night_color_combo(entered_text: str, entered_style: str):
    local_colors = (
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA,
        Fore.BLACK, Fore.LIGHTBLACK_EX, Fore.WHITE, Fore.MAGENTA
    )

    return pattern_color_combos(
        pattern_colors=local_colors, pattern_text=entered_text,
        pattern_style=entered_style
    )
