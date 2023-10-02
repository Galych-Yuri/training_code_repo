# ----------------------------------------------------------------
def print_list(*args):
    print(args)


print_list(1, 2, 3, 4)


# (1, 2, 3, 4)


# ----------------------------------------------------------------
def full_func(*args, **kwargs):
    print(args)
    print(kwargs)


full_func(1, 2, 3, a=4, b=5, c=6)


# {'a': 4, 'b': 5, 'c': 6} і фіг знає що вона робить!


# ----------------------------------------------------------------
def pizdec(*args):
    # *args - приймає будь-яку кількість позицийних аргументів. Повертає результат у вигляді кортежу
    print(args)
    for iterator in args:
        print(iterator)


pizdec(1, 2, 3, 4, 5, 100)


# (1, 2, 3, 4, 5, 100)

# 1
# 2
# 3
# 4
# 5
# 100


# ----------------------------------------------------------------
def piz(**kwargs):
    print(kwargs)
    for iterator in kwargs:
        print(iterator)


# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# **kwargs - приймає будь-яку кількість іменованих аргументів. Повертає результат у вигляді словника

print(type(piz(a=1, b=2, c=3, d=4)))


# <class 'NoneType'>

# a
# b
# c
# d
# --------------------------------


# Цю функцію називають "збiр аргументів у словник" хоча вона видає хуйню.
def another_kwargs_func(**kwargs):
    keys, values = [], []
    for key, value in kwargs.items():
        # print(key, value)
        keys.append(key)
        values.append(value)
    return keys, values


keys, values = another_kwargs_func(a=5)
print(keys, values)  # ['a'] [5]

# a 5

# ------------------------------

def lite_kwargs_function(**kwargs):
    # print(kwargs)
    return kwargs
    # for iterator in kwargs:
    # print(iterator)
    # print(kwargs[iterator])


example_kwargs_dict = lite_kwargs_function(a=2, b=7, t=3)
print(example_kwargs_dict)  # {'a': 2, 'b': 7, 't': 3}


# -----------------------------

# У функції нижче є обмеження:
# - спочатку *, потім **
# - виклик функції такий самий: спочатку позиційні аргументи (*), а потім (**) іменовані аргументи
def full_func(*args, **kwargs):
    return args, kwargs


some_result = full_func(1, 2, 3, a=4, b=5, c=6)
print(some_result)
# ((1, 2, 3), {'a': 4, 'b': 5, 'c': 6})
# Тобто воно повертає кордеж в якому два індекса. за нульовим індексом кортеж з неіменованими аргументами,
# а за першим інжексом класичний свловник

some_result_1 = full_func(1, 2, 3)
print(some_result_1)
# ((1, 2, 3), {})
# А тут ця функція повертає позиційні аргументи, які ми вказали при виклику функці та порожній словник,
# що можливо буде якось корисно для майбутньої взамодії з ним, але не зробумило як до нього звертатися.
# Можливо через індекси?

print(full_func())
# ((), {})

