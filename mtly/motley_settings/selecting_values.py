from mtly.motley_settings import (
    Colors, Styles, ColorCombos, volcano, fresh, night
)


def selecting(
        entered_style: Styles,
        entered_color: Colors,
        entered_color_combo: ColorCombos) -> str:
    """
    :return: str
    - исходя из того, какой цвет и какую комбинацию выбрал пользователь,
        сообщение (о том, что он указал сразу 2 этих параметра)
            будет кастомизировано
        - в этом сообщении слово `цвет` будет иметь такой же цвет,
            как и указал пользователь
        - также будет и с цветовой комбинацией
    """
    return (entered_style.value +
            (f"{Colors.WHITE.value + 'Вы указали сразу и '}"
                            f"{entered_color.value + 'цвет'}" 
                            f"{entered_color.WHITE.value + ', и'} "
            f"{volcano("цветовую комбинацию")
                if '.' not in f'{entered_color_combo}'[-7:].lower()
                else fresh("цветовую комбинацию")
                    if f'{entered_color_combo}'[-5:].lower() == "fresh"
                    else night("цветовую комбинацию")}"))
