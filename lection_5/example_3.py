# in while loop - якщо весь цикл виконується коректно, то далі виконується else. Якщо був break,
# то else не буде виконуватися


target = input("Enter a number: ")
lists = ["112", 45, 56, "rrr", None]

index = 0
while index < len(lists):
    if str(lists[index]) == target:
        break
    index += 1
else:
    index = -1

print(f"Index is: {index}")
