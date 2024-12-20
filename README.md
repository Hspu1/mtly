# ***mtly***
### - *Библиотека для кастомизации текста*
#
##
# **Быстрый старт**
> # ```pip install mtly```
#
##
# **Примеры использования**
### *Давайте запустим следующий код:*
```python
from mtly import *


print(motley(text="HELLO WORLD", color=Colors.GREEN, style=Styles.BOLD_ITALIC))
print(motley(text="HELLO WORLD", color=Colors.DARK_GREEN, style=Styles.BOLD_ITALIC))
print(motley(text="HELLO WORLD", color=Colors.LIGHT_BLUE, style=Styles.BOLD_ITALIC))
print(motley(text="HELLO WORLD", color=Colors.BLUE, style=Styles.BOLD_ITALIC))
print(motley(text="HELLO WORLD", color=Colors.DARK_BLUE, style=Styles.BOLD_ITALIC))
print(motley(text="HELLO WORLD", color=Colors.YELLOW, style=Styles.BOLD_ITALIC))
print(motley(text="HELLO WORLD", color=Colors.ORANGE, style=Styles.BOLD_ITALIC))
print(motley(text="HELLO WORLD", color=Colors.RED, style=Styles.BOLD_ITALIC))
print(motley(text="HELLO WORLD", color=Colors.PINK, style=Styles.BOLD_ITALIC))
print(motley(text="HELLO WORLD", color=Colors.DARK_PINK, style=Styles.BOLD_ITALIC))
print(motley(text="HELLO WORLD", color=Colors.PURPLE, style=Styles.BOLD_ITALIC))
print(motley(text="HELLO WORLD", color=Colors.DARK_PURPLE, style=Styles.BOLD_ITALIC))
print(motley(text="HELLO WORLD", color=Colors.GREY, style=Styles.BOLD_ITALIC))
print(motley(text="HELLO WORLD", color=Colors.BLACK, style=Styles.BOLD_ITALIC))
print(motley(text="HELLO WORLD", color=Colors.WHITE, style=Styles.BOLD_ITALIC))


(
    print(), print(motley(text=".", color=Colors.RED, style=Styles.BOLD_ITALIC)*5,
               motley(text=".", color=Colors.GREEN, style=Styles.BOLD_ITALIC)*5,
               motley(text=".", color=Colors.RED, style=Styles.BOLD_ITALIC)*5,
               motley(text=".", color=Colors.GREEN, style=Styles.BOLD_ITALIC)*5),
 print(motley(text=".", color=Colors.GREEN, style=Styles.BOLD_ITALIC)*5,
       motley(text=".", color=Colors.RED, style=Styles.BOLD_ITALIC)*5,
       motley(text=".", color=Colors.GREEN, style=Styles.BOLD_ITALIC)*5,
       motley(text=".", color=Colors.RED, style=Styles.BOLD_ITALIC)*5),
     print()
)


print(motley(text="WASSUP", color_combo=ColorCombos.VOLCANO, style=Styles.BOLD))
print(motley(text="WASSUP", color_combo=ColorCombos.FRESH, style=Styles.BOLD))
print(motley(text="WASSUP", color_combo=ColorCombos.NIGHT, style=Styles.BOLD))


(
    print(), print(motley(text=".", color=Colors.RED, style=Styles.BOLD_ITALIC)*5,
               motley(text=".", color=Colors.GREEN, style=Styles.BOLD_ITALIC)*5,
               motley(text=".", color=Colors.RED, style=Styles.BOLD_ITALIC)*5,
               motley(text=".", color=Colors.GREEN, style=Styles.BOLD_ITALIC)*5),
 print(motley(text=".", color=Colors.GREEN, style=Styles.BOLD_ITALIC)*5,
       motley(text=".", color=Colors.RED, style=Styles.BOLD_ITALIC)*5,
       motley(text=".", color=Colors.GREEN, style=Styles.BOLD_ITALIC)*5,
       motley(text=".", color=Colors.RED, style=Styles.BOLD_ITALIC)*5),
     print()
)


print(motley(text="INTERESTING", color=Colors.BLUE,
             color_combo=ColorCombos.FRESH, style=Styles.ITALIC))
```
## **На выходе получим нечто прекрасное:**
![](https://iimg.su/s/19/3Nt0cxXPnWPmv6A7ewnYsV7g5VW7PRIbBjZ6xOuy.png)
> ## **Здесь мы наблюдаем 15 цветов, 3 цветовые комбинации и 3 стиля в действии**
####
> > ### *За каждым из необязательных параметров функции motley стоит специальный класс:*
> ###
> > ### **Colors - отвечает за все цвета**
> > ###
> > #### *зеленый, темно-зеленый, светло-синий, синий, темно-синий,* 
> > #### *желтый, оранжевый, красный, розовый, темно-розовый (лососевый),*
> > #### *фиолетовый, темно-фиолетовый, серый, черный, белый*
> ### 
> > ### **ColorCombos - отвечает за все цветовые комбинации**
> > #####
> > #### *вулкан, свежий, ночь*
> ### 
> > ### **Styles - отвечает за все стили**
> > ##### 
> > #### *курсив, жирный, жирный курсив, нормальный*
#### 
> ## **Вы можете их использовать так, как захотите!**
# 
## 
# **FAQ**
## `Чем mtly лучше colorama???`
###
## *В отличие от нее, mtly - удобная библиотека*
####
### *При использовании colorama вы сталкиваетесь со множеством проблем:*
###
### *1) Несоответствие цветов*
> #### *- из того, что сразу приходит в голову: белый цвет вдруг стал темно-фиолетовым,*
> #### *- огромные несостыковки с тёплыми цветами*
###
### *2) Непонятные название классов и констант классов*
> #### *- зачем класс, которые отвечает за цвета, называть Fore (англ. "Передний")?*
> #### *- опять-таки, из того, что сразу приходит на ум: жирный шрифт почему-то стал ярким*
### 
### *3) Громоздкость использования*
> #### *- чтобы применить какой-либо цвет/стиль, мне нужно прописать некую конструкцию,*
> #### *где нужно соблюсти определённый порядок, о котором я, как пользователь, не имею ни малейшего понятия*
> #### *(пример: стиль не будет применён к тексту, если записать конструкцию как "текст" + "стиль",*
> #### *нужно написать "стиль" + "текст")*
###
### *4) Функционал*
> #### *я захожу на минное поле, но всё же попытаюсь аргументировать свою позицию:*
> #### *- в "колораме" нет никаких цветовых комбинаций, а вследствие и доп функции (цвет + комбо)*
> #### *- в ней также нет таких шрифтов (стилей) как: курсив, жирный курсив*
#
## *Однако, в colorama есть огромное количество функций, которых нет в mtly*
###
> ### *И я бы рассматривал свою библиотеку как урезанную и усовершенствованную копию вышеупомянутой "колорамы"*
> ### *Так как функции в моей реализации (так скажем) покрывают большинство нужд пользователей,*
> ### *решивших увидеть в консоли что-нибудь цветное*
