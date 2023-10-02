from _datetime import datetime


new_start_timer = datetime.now()
lite_list_of_numbers = list(range(1, 15))
slices_time_1 = datetime.now() - new_start_timer
print(lite_list_of_numbers)
print(f"The lite list range generator is: ({slices_time_1}) seconds")

# Складний генератор списків запропонований лектором.

timers = datetime.now()
list_of_numbers = [iterator for iterator in range(1, 15)]
slices_time_2 = datetime.now() - timers
print(list_of_numbers)
print(f"The Syntax sugar crate list of numbers is: {slices_time_2} seconds")

# Сама по собі конструкція займає більше часу, бо виконуємо перебір значень. Але якщо цукор буде щось математичити

list_cube_numbers = [iterator**2 for iterator in range(1, 15)]
print(list_cube_numbers)
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196]
# ----------------------------------------------------------------

first_list = ["1", "2", "3", "4", "5", "a4", "b4", "c4", "d4", "e"]
print(first_list)  # ['1', '2', '3', '4', '5', 'a4', 'b4', 'c4', 'd4', 'e']

second_list = [iterator for iterator in first_list if iterator.isdigit()]
print(second_list)  # ['1', '2', '3', '4', '5']

third_list = [iterator for iterator in first_list if iterator.isalpha()]
print(third_list)  # ['e']
# ----------------------------------------------------------------

old_dict = {"ds": 1, "sds": 2, "cccc": 3}

new_dict = {key + str(len(key)): value**2 for key, value in old_dict.items()}
print(new_dict)  # {'ds2': 1, 'sds3': 4, 'cccc4': 9}

new_dict_2 = {len(key): value**2 for key, value in old_dict.items()}
print(new_dict_2)  # {2: 1, 3: 4, 4: 9}

# ----------------------------------------------------------------

