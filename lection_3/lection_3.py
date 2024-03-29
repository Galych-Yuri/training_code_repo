# source training_code_venv/bin/activate


tuples = (1, 2, 3, 4, "5")
print(len(tuples))  # 5
print(tuples[2])  # 3 Якщо ми хочемо звернутися до конкретного елемента в кортежі, то потрібні []
print(tuples[-1::-1])  # reverse = ('5', 4, 3, 2, 1)


# run file in terminal - python lection_3.py


lists = list((1, 2, 3, 4, "5"))
crazy_lists = [3, 2, 'we', [14, 5, 6, (True, False)], None]
print(crazy_lists[3][3][0])  # True


# Звернення до методів кожного обʼєкту  відбувається через крапку (.)
crazy_lists[3].append('0')  # Через індекс вставляємо у вкладений список стоку з нулем
print(crazy_lists)  # [3, 2, 'we', [14, 5, 6, (True, False), '0'], None]
del crazy_lists[4]  # -None  [3, 2, 'we', [14, 5, 6, (True, False), '0']]
print(crazy_lists)


crazy_tuple = (1, 2, [3, 4, 5])
crazy_tuple[2].remove(3)  # Не дивлячись на те що кортежі незмінні, як що в них є змінний тип даних, то його можна
# редагувати. Тобто повністю видалити вкладений список не вийде, він, якщо ми так зробимо залишиться порожнім,
# але видалити чи додати туди щось ми так.
print(crazy_tuple) # (1, 2, [4, 5])


# Метод extend() може приймати в себе змінну загорнуту в список
lists.extend(crazy_lists)
print(lists)  # [1, 2, 3, 4, '5', 3, 2, 'we', [14, 5, 6, (True, False), '0']]
lists.extend([crazy_lists])
print(lists)  # [1, 2, 3, 4, '5', [3, 2, 'we', [14, 5, 6, (True, False), '0']]]
# Як бачимо він обʼєднав списки і другий варіант став більш відокремленим
# Але для такої операції праще використовувати .insert(index, variable) і тоді можна не ставити квадратні дужки
# .insert(index, variable) - просто вставляє. Тобто працює швидше
# .extend(variable) - розширяє інстуючий список, але перед операцією він його розпакує. Тобто витратить більше ресурсів на його обробку
# .append() - Теж додає елемент до списка повністю, тож краще все ж .insert(index, variable)


# set() - зберігає індекси у хеш-таблиці. Хеш таблиця - 16-символів на один елемент.
# в множину можна записувати тільки незмінний тип даних. Тобто список не можна, а кортеж можна


dictionary = {
    1: lambda a, b: a * b, 2: lambda a, b: a - b, 3: lambda a, b: a / b, 4: lambda a, b: a % b, 5: lambda a, b: a + b
}
dict_keys = dictionary.keys()
dict_keys = list(dict_keys)
print(dict_keys)  # [1, 2, 3, 4, 5]
# Отримали список ключів і можемо проводити з ними якісь маніпуляції. Тільки навіщо?
# є ще команди .values() значення; .items() its key_and_value

# Коли ми створюємо незмінний тип даних, типу кортеж, то в памʼяті записується по силання на нього
# Коли ми створюємо змінній   тип даних, типу список, то в памʼяті кожен раз записується цей тип даних і айді до нього
# рекомендують користуватися методом (import copy) .kopy() він створює копію яку можна змінювати, а оригінал
# не зазнає змін, якщо обидві змінні посилаються на один і той самий елемент.
# Якщо справи кепськи юзаємо (import copy) deepcopy().


variable_str_on_int = (int("1" + "2") + 1)  # 13 -  Тому що, спочатку виконається конкатенація рядків, потім вони
# поміняють тип даних зі str on int і далі додасться 1.


# Непоганий спосіб почистити список від елементів які повторюються
new_list = [1, 1, 2, 3, 3, 4, 4, 5, 5]
new_unic_list = list(set(new_list)).sort()
print(new_unic_list)  # [1, 2, 3, 4, 5]


