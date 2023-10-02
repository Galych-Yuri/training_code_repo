# Дан словарь, создать новый словарь при помощи конструкции генератор словаря,
# поменяв местами ключ и значение.

dictionary = {"add": "concatenate", "sub": "substract"}


def swap_keys_and_values(input_dict):
    swapped_dict = {v: k for k, v in input_dict.items()}
    return swapped_dict


swapt_dictionary = swap_keys_and_values(dictionary)
print(swapt_dictionary)  # {'concatenate': 'add', 'substract': 'sub'}





