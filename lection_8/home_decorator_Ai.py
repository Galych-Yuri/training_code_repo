from datetime import datetime

timer = datetime.now()
print(f"Initializing timer {datetime.now() - timer}")

user_input = input("Введіть деякий текст: ").lower().strip()
user_input = user_input.split()
print(f"Працюємо з таким набором тексту:\n{user_input}")


def cheker_timers(func):
    """
    Вимірює час виконання функції
    """

    def wrapper(*args, **kwargs):
        time = datetime.now()
        result = func(*args, **kwargs)
        print(f"Функція виконана за: {datetime.now() - time} секунд.")
        # print(f"The kwargs: {kwargs}")
        # print(f"The args: {args}")
        return result

    return wrapper


@cheker_timers
def reverse(params: list) -> list:
    """
    Повертає зворотній список
    """
    params.reverse()
    return params


@cheker_timers
def word_reverse(word: list) -> list:
    """
    Повертає список слів зі зворотньою послідовністю букв
    """
    iter_lst = []
    for iterator in word:
        iter_lst.append(iterator[-1::-1])
    return iter_lst


print(reverse(user_input))
print(word_reverse(user_input))
