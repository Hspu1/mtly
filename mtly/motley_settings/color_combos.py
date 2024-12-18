from colorama import Fore


def pattern_color_combos(
        pattern_colors: tuple,
        pattern_text: str
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

    return new_text


def volcano(entered_text: str):
    local_colors = (
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX,
        Fore.LIGHTRED_EX, Fore.WHITE, Fore.YELLOW,
        Fore.LIGHTBLACK_EX, Fore.LIGHTYELLOW_EX

    )

    return pattern_color_combos(
        pattern_colors=local_colors, pattern_text=entered_text
    )


def fresh(entered_text: str):
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
        pattern_colors=local_colors, pattern_text=entered_text
    )


def night(entered_text: str):
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
        pattern_colors=local_colors, pattern_text=entered_text
    )
