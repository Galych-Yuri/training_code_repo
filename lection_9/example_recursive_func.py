from datetime import datetime

user_number = input("Enter a number: ")  # 5


# Decorator for time checking
def check_time(func):
    def wrapper(*args, **kwargs):
        time_start = datetime.now()
        result = func(*args, **kwargs)
        time_end = datetime.now()
        print(f"Function was called. Input is: {user_number} Result is: {result} Time was: {time_end - time_start}")

        return result

    return wrapper


# Classic functions

@check_time
def factorial(param: int) -> int:
    counter = 0
    result = 1
    while param > counter:
        counter += 1
        result *= counter

    return result


# ----------------------------------------------------------------

# Recursive functions. When function is called itself

@check_time
def factorial_2(param: int) -> int:
    if param == 0:
        return 1
    else:
        return param * factorial_2(param - 1)
        # return 5 * 4 * 3 * 2 * 1 * 1


print(factorial(int(user_number)))  # 120
print(factorial_2(int(user_number)))  # 120

# Мoжна випадково потрапити у вічний цикл і тоді памґять закінчиться. Бо коли така функція працює - всі її
# виклики, а в нашому випадку 5 чи 6 викликів будуть висіти в памʼяті компа.
