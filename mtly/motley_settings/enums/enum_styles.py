from enum import StrEnum, unique


@unique
class Styles(StrEnum):
    ITALIC = "\x1B[3m"
    BOLD = "\x1B[1m"
    BOLD_ITALIC = "\x1B[1;3m"
    DEFAULT = "\x1B[0m"
