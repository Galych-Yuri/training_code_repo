some_dict = {1: "a", 2: "b", 3: "c"}

for iteration in some_dict:
    print(some_dict[iteration])

# a
# b
# c

generator_list = list(range(10))

first_value, second_value, *third_value = generator_list

print(third_value)  # [2, 3, 4, 5, 6, 7, 8, 9]

"""Одна функція - одна дія"""


def example(param_1, param_2, param_3, **kwargs):
    print(param_1, "is parameter 1")
    print(param_2, "is parameter 2")
    print(param_3, "is parameter 3")
    print("Kwargs is:", kwargs)


example(1, 2, 3, b=1, c=2, d=3)


# 1 is parameter 1
# 2 is parameter 2
# 3 is parameter 3
# Kwargs is: {'b': 1, 'c': 2, 'd': 3}

def dont_do_this():
    for iteration in some_dict:  # Не використовувати глобальні змінні у функції. Це типу може погано закінчитися?
        pass


# Краще прокидати через функцію цілу змінну

def do_this(for_some_dict):
    for iteration in for_some_dict:
        pass


do_this(some_dict)
# Тоді ітерується не сама змінна, а її значення. Тобто вона стає іншою змінною (for_some_dict)
# в локальній області видимості. А от і ніфига. Якщо це змінний тип даних. то треба робити deep_copy

import copy

do_this(copy.deepcopy(some_dict))  # отак буде збс, якщо ми маємо справу зі змінним типом даних
