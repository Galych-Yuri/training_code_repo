# Дан список чисел.
# Посчитать сколько раз встречается каждое число. Использовать для подсчёта функцию.
# Подсказка: для хранения данных использовать словарь (ключ - само число, а значение - сколько раз оно встречается).
# Для проверки нахождения элемента в словаре использовать метод get(), либо оператор in.


list_for_dictionary = list(range(10))


def get_dictionary(lst):
    return {lis: len(str(lis)) for lis in lst}


# def get_dictionary(lst):
#     return {item: len(str(item)) for item in lst}


print(get_dictionary(list_for_dictionary))
# {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
