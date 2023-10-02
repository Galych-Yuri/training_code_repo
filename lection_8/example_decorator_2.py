def my_decorator(a_func):
    def the_wrapper():
        print("Before")
        a_func()
        print("After")

    return the_wrapper


@my_decorator
def alone_function():
    print("Print some text...")


# alone_function = my_decorator(alone_function)  # Так теж можна!
# alone_function_wrapper = my_decorator(alone_function)
# alone_function_wrapper()
# Before
# Print some text...
# After

# Для того аби не визначати окрему змінну alone_function_wrapper
# і у ній не крутити значення, можна запхати знак (@)
# і поставити після нього назву функції-декоратора. І ця конструкція
# розміщується над функцією яка буде використовуватися під і просто викликати залежну

print(50 * "-")
alone_function()
# Before
# Print some text...
# After


# А тепер що тут відбувається. У нас є функція, яка приймає в якості агрумента функцію, виконує якийсь
# код до функції, викликає функцію, виконує код після виклику функції
