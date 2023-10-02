"""
Надрукувати перший рядок
Надрукувати пʼятий рядок
Надрукувати перші пʼять рядків
Надрукувати весь файл
"""

f = open("code_lector/test.txt")

data_a = f.readline()
print(f"First line: \"{data_a}\"")
f.close()

print(50 * "-")
# --------------------------------

f = open("code_lector/test.txt")
for count, iteration in enumerate(f):
    if count == 4:
        print(f"Five line printed: (\"{iteration}\")")
f.close()

print(50 * "-")
# --------------------------------

f = open("code_lector/test.txt")
for count, iteration in enumerate(f, start=1):
    if count < 6:
        print(f"Line: {count}; contain: ({iteration})...", end=" ")
f.close()

print(50 * "-")
# --------------------------------

with open("code_lector/test.txt") as f:
    text_data = f.readlines()
    for iteration in text_data:
        print(iteration, end="")

print(50 * "-", sep="\n", end="\n")
# --------------------------------


