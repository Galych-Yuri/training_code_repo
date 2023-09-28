print(1 % 3 == 0)

user_number = int(input("Enter the value: "))

counter = 1
index = 1
result_2 = 0

while counter < user_number:
    if counter % 3 == 0:
        continue
    index = counter ** 3
    result_2 += index
    counter += 1
print(f"Total sum: {result_2} ")

