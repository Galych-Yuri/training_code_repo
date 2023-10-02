"""
Дан список состоящий из данных разного типа.
Вернуть новый список, где при помощи функции map() каждый элемент типа int первоначального списка приведён
к типу str, элементы всех остальных типов передаются в новый список без изменения их типа.
В качестве входной функции в map() использовать lambda-функцию.

values = [1, 2, '3', 'forth', 'end', 99, True, None]

"""

values = [1, 2, '3', 'forth', 'end', 99, True, None]

# changed_values = list(map(lambda x: str(x) if isinstance(x, int) else x, values))
changed_values_1 = list(map(lambda x: str(x) if type(x) == int else x, values))

print(values)
# print(changed_values)
print(changed_values_1)
