
"""
Ввести з клавіатури ціле число n.
Одержати суму кубів усіх цілих чисел від 1 до n(включно з n). Винятки становлять усі числа кратні цифрі 3.
Реалізувати в 2-х варіантах: використовуючи цикл while і цикл for
"""

user_number = input("Please enter a number: ")

if not user_number.isdigit() or int(user_number) == 0:
    print("Your input is incorrect! Program is disabled.")
    quit()

result = 0

for digit in range(1, int(user_number)+1):

    if digit % 3 == 0:
        continue
    else:
        result = digit ** 3
        print(f"Counter is: {result}.")

# ----------------------------------------------------------------
# Mentor

# value = int(input("Enter the value: "))

sum_1 = 0
for i in range(1, int(user_number)+1):
    if not i % 3 == 0:
        i **= 3
        sum_1 += i
print(f"Total sum: {sum_1} ")

print(4 ** 3)