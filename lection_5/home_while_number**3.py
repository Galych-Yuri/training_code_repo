"""
Ввести з клавіатури ціле число n.
Одержати суму кубів усіх цілих чисел від 1 до n(включно з n). Винятки становлять усі числа кратні цифрі 3.
Реалізувати у 2-х варіантах: використовуючи цикл while і цикл for
"""

user_number = input("Please enter a number: ").strip()

counter = 1
result = 0

while counter <= int(user_number):

    if counter ** 3 and counter % 3 == 0:
        counter += 1
    else:
        result = counter ** 3

    counter += 1

    print(f"Counter is {counter}")
    print(f"Result is {result}")

print(f"Your {user_number} number ** by 3 give result: {result}.")

# Doesnt work with while loop
# ----------------------------------------------------------------
# Mentor answers

counter = 0
i = 1
sum_2 = 0
while counter < int(user_number):
    counter += 1
    if counter % 3 == 0:
        continue
    i = counter**3
    sum_2 += i
print(f"Total sum: {sum_2} ")
