# Анотації потрібні => щоб підвищити інформативність коду і зазвичай пояснюють що той чи інший фрагмет коду буде робити
# Це покищо корисно на прикладі функцій. Можливо дейсь ще використовується


def say_hi_name(name: str) -> str:
    return f"Hi {name}"


# .__annotations__ - це метод який дозволяє іншим розробникам продуктивніше читати твій код
print(say_hi_name.__annotations__)  # {'name': <class 'str'>, 'return': <class 'str'>}
# Якщо прибрати останній (str) то поверне: {'name': <class 'str'>}
# Якщо прибрати перший (str) то повернеЖ   {'return': <class 'str'>}


def hello(name: str, age: int = 6):
    return f"Hello, {name}, your age is {age}"


print(hello("Grabli"))  # Hello, Grabli, your age is 6
