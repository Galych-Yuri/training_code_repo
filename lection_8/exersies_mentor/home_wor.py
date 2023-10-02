# Даний список, що складається з даних різного типу.
# Повернути новий список, де за допомогою функції map() кожен елемент типу
# int початкового списку приведений до типу str, елементи решти всіх типів
# передаються в новий список без зміни їх типу.
# У якості вхідної функції в map використовувати lambda-функцію.


values = [1, 2, '3', 'forth', 'end', 99, True, None]

new_value = list(map(lambda x: str(x) if isinstance(x, int) and not isinstance(x, bool) else x, values))

print(new_value)

# ----------------------------------------------------------------

# За допомогою функції filter() з котрежу слів відфільтрувати тільки ті,
# які є поліндромами (які однаково читаються в обидві сторони), регістр
# літер не враховувати.


inputdata = ('Країна', 'шалаш', 'Летел', 'вертольот', 'УЧУ', 'мем', 'мова')

polindroms = list(filter(lambda word: word.lower() == word[::-1].lower(), inputdata))
print(polindroms)

# ----------------------------------------------------------------

# Написати декоратор до 2-х будь-яких функцій, який би вважав та виводив
# час їх виконання.
# Підсказка:
# from datetime import datetime
# now = datetime.now()


from datetime import datetime
import time


def dec_time_measure(func):
    def wrapper():
        start = datetime.now()
        func()
        end = datetime.now()
        print(f"Время выполнение функции {func}: {end - start} секунд")

    return wrapper


@dec_time_measure
def testFunc1():
    print("Выполняется функция testFunc1")
    time.sleep(1)
    print("Функция testFunc1 выполнена")


@dec_time_measure
def testFunc2():
    print("Выполняется функция testFunc2")
    time.sleep(2)
    print("Функция testFunc2 выполнена")


testFunc1()
testFunc2()
