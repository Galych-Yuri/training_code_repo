"""
Написати декоратор до 2-х будь-яких функцій, який би рахував і виводив час їхнього виконання.
Підказка:
from datetime import datetime
time = datetime.now()
"""

from datetime import datetime


user_input = input("Enter some text: ").lower().strip()
user_input = user_input.split()


def cheker_timers(func):
    time = datetime.now()
    func()
    print(f"The function work: {datetime.now() - time} seconds.")


@cheker_timers
def reverse(params: list) -> list:
    """
    return reverse list
    """

    params.reverse()
    return params


print(reverse(user_input))


# Biba piba tuchuka kalva abda

@cheker_timers
def word_reverse(word: list) -> list:
    iter_lst = []
    for iterator in word:
        iter_lst.append(iterator[-1::-1])

    return iter_lst


print(word_reverse(reverse(user_input)))



