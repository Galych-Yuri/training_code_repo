# for cycles

user_number_input = input("Enter a number: ")
list_of_items = ["112", 45, 56, "rrr", None]

index = 0

for item in list_of_items:
    if str(list_of_items[index]) == user_number_input:
        break
    index += 1
else:
    index = -1

print(f"Index what you looking in ' ' is: {index}")
# but there is mistakes in if lst[index], we cant check numbers, just strings
# so we add STR in if stage - str(list_of_items[index])

# ----------------------------------------------------------------

for count, iterator in enumerate(list_of_items):
    if str(iterator) == user_number_input:
        break
else:
    count = -1

print(f"Index what you looking in 'lists_of_items' is: {count}")
