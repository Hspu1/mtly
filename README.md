# **mtly**
### - *Библиотека для кастомизации текста*
#
##
## **Быстрый старт**
> ### *для установки просто напишите в терминале*
> # ```pip install mtly```
#
##
## **Примеры использования**
### *Для начала нужно импортировать функцию motley, которая и будет выполнять всю работу*
>    ```python
>    from mtly import motley
>    ```
####
## **14 цветов, 3 цветовые комбинации и 3 стиля**
### *Вы можете комбинировать их как зах хотите*
```python
from mtly import motley


print(motley(text="Все цвета:"))
print(f'{motley(text="green")}: {motley(text="Hello World", color="green")}')
print(f'{motley(text="dark_green")}: {motley(text="Hello World", color="dark_green")}')
print(f'{motley(text="light_blue")}: {motley(text="Hello World", color="light_blue")}')
print(f'{motley(text="blue")}: {motley(text="Hello World", color="blue")}')
print(f'{motley(text="dark_blue")}: {motley(text="Hello World", color="dark_blue")}')
print(f'{motley(text="yellow")}: {motley(text="Hello World", color="yellow")}')
print(f'{motley(text="orange")}: {motley(text="Hello World", color="orange")}')
print(f'{motley(text="pink")}: {motley(text="Hello World", color="pink")}')
print(f'{motley(text="dark_pink")}: {motley(text="Hello World", color="dark_pink")}')
print(f'{motley(text="red")}: {motley(text="Hello World", color="red")}')
print(f'{motley(text="purple")}: {motley(text="Hello World", color="purple")}')
print(f'{motley(text="dark_purple")}: {motley(text="Hello World", color="dark_purple")}')
print(f'{motley(text="grey")}: {motley(text="Hello World", color="grey")}')
print(f'{motley(text="black")}: {motley(text="Hello World", color="black")}')

print()

print(f'{motley(text="Все цветовые комбинации:")}')
print(f'{motley(text="fresh")}: {motley(text="Hello World", color_combo="fresh")}')
print(f'{motley(text="volcano")}: {motley(text="Hello World", color_combo="volcano")}')
print(f'{motley(text="night")}: {motley(text="Hello World", color_combo="night")}')

print()

print(f'{motley(text="Все стили:")}')
print(f'{motley(text="bold")}: {motley(text="Hello World", style="bold")}')
print(f'{motley(text="italic")}: {motley(text="Hello World", style="italic")}')
print(f'{motley(text="bold_italic")}: {motley(text="Hello World", style="bold_italic")}')

print()

print(motley(text="Пример с использованием различных цветов и стилей:"))
print(
    motley(text="123", color="light_blue", style="italic"),
    motley(text="456", color="blue", style="bold"),
    motley(text="789", color="dark_blue", style="bold_italic")
)

print()


print(motley(text="Пример с использованием различных цветовых комбинаций и стилей:"))
print(motley(text="123456789", color_combo="fresh", style="bold_italic"))
print(motley(text="123456789", color_combo="volcano", style="bold_italic"))
print(motley(text="123456789", color_combo="night", style="bold_italic"))
```
### ***Запустите этот код и вам всё станет понятно!***
