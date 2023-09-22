
print("Hell, world!")

print("Add new line")

print("Add new new message")

add_message = "Hi there!"

some_message = "Hello, world!"

number_x = "0x" "16-hічна система ісчісленія"

number_b = "0b" "двійкова система"

print("%.10f" % 5.4)  # 5.4000000000
print("%.20f" % 5.4)  # 5.40000000000000035527

number_float = "Умовно точне, але після 15 десь знака починають зявлятися не нулі. Тобто такі числа є приблизними "

print(10 % 3)  # 1

div_mod = divmod(10, 3)  # Виконує два види ділення одного і того ж виразу. Спочтку %, а потім //.
print(div_mod)  # (3, 1)

round_number = round(3.14159, 2) # 3.14 Другий параметр відповідає за відображення кількості знаків після коми.

multiply_x2 = 2**2**3, "Піднесення до степеня відбувається з права на ліво"
print(multiply_x2)  # 256

# change value in variables
a = 1
b = 2
a, b = b, a

import os

concurrent_directory = os.getcwd()
print("Directory is:", concurrent_directory)
print(os.listdir(concurrent_directory))  # яки файли чи папки є в середині

"""
pip uninstal назва_бібліотеки - то можна делітнути непотрібні чи зайві бібліотеки

Поряд з проєктом створюється файл RECUAREMENTS.txt кузи записуються всі залежності програми від різноманітних бібіотек які використовуються в проєкті. 

pip freeze > "file_name" - і наприклад ми вкажемо (1.тхт) і туди автоматом запишуться всі залежності

як їх підтягувати?
pip install -r 1.txt - це піпка залізе в куди вказали і сам підтягне та встановить потрібні бібліотеки 
"""


