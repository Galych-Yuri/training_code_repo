# Декоратор це теж синтаксичний цукор. Він бере якусь функцію


def some_function(word="Yes"):
    return word + "!"


print(some_function())  # Yes!

same_some_function = some_function

print(same_some_function())  # Yes!


# ----------------------------------------------------------------

def strepsils(func):
    print("Before")
    print(func())
    print("After")


strepsils(same_some_function)
# Before
# Yes!
# After
