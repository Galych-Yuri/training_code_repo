# Документування. Опис функціїї та її параметрів які вона може приймати

def hello(name, age=6):
    """
    Print "Hello,{name}, your age is {age}"
    """
    return f"Hello, {name}, your age is {age}"


print(hello.__doc__)  # doctest: Print "Hello,{name}, your age is {age}"
print(hello)  # <function hello at 0x102d8b5b0>


# ----------------------------------------------------------------

# Lambda functions - одноразова функція. Використовується у якості вхідних функцій для інших функцій.

# Рахуємо площу трикутника


def area(b, h):
    return 0.5 * b * h


triangle_area = lambda b, h: 0.5 * b * h

print(area(2, 4))  # 4.0
print(triangle_area(2, 4))  # 4.0

# В lambda не можна використовувати умови та цикли
