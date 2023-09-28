first_name = "Євген"
second_name = "Арефа"
second_name = second_name[-1::-1].title()
print(second_name)  # Афера


user_first_name, user_second_name = (input("Enter your first name: ").lower(),
                                     input("Enter your second name: ").lower())

user_first_second_name = input("Enter your first and second name: ").lower().capitalize()
user_first_second_name = user_first_second_name.strip()

print(user_first_name.title(), user_second_name.title(), user_first_second_name.title())


q, w, e, r = "spam"  # q = "s", w = "p", e = "a", r = "m"

list_of_four_values = ["s", "p", "a", "m"]
t, y, u, i = list_of_four_values  # s p a m
o, *p = list_of_four_values
print(o)  # s
print(p)  # ['p', 'a', 'm']
a = s = [1, 2, 3]  # same id, group assign
"""
print function
print(*objects, sep=' ', end='\n', file=name_variable, flush=False)
sep=' ' - start seperetor. роздільник для виводу обєктів
end='\n' - end seperator. визначає поведінку. В даному випадку з нової строки
"""

create_file = open("../python.txt", "a")
# w - режим запису (взагалі перезапису, тобто коли відкриє файл в якому
# вже щось є, то воно видалить данні з нього і запише нові)
# а - режим дозапису
print("Hello, world", sep="", end=",", file=create_file)
create_file.close()  # будьякий файл обовʼязково потрібно закривати після використання,
# бо інакше це зробить прибиральник і дані можуть не дозаписатися, а файл буде заблокований.


import datetime  # to use some modul need: datetime.datetime.
# from datetime import datetime - import just second_datetime and if i need to call: datetime.now()

time_now = datetime.datetime.now()
name = "Biba"
age = 0.6
print("Mv name is %s. I'm is %d ears old. %s is good nome" % (name, age, name))
print("Mv name is %(name)s. I'm is %(age)d ears old. %(name)s is good nome" % {"name": name, "age": age})
print("Mv name is {}. I'm is {} ears old. {} is good nome".format(name, age, name))
print("Mv name is {0}. I'm is {1} ears old. {0} is good nome".format(name, age))
print("Mv name is {name}. I'm is {age} ears old. {name} is good nome".format(name=name, age=age))
print(f"Mv name is {name}. I'm is {age} ears old. {name} is good nome")
time_after = datetime.datetime.now()
create_file = open("../python.txt", "a")
print(f"Program is working with % (name, age, name) {time_after - time_now}", end="\n", file=create_file)
create_file.close()

# ще один спосіб заміряти час - це вивести час на зараз командою (datetime.datetime.now()) та відняти від нього
# змінну з заміряним часом. Тількаи чомусь красотуль цю змінну розмістив спочатку
"""
time_now = datetime.datetime.now()
print("Mv name is %s. I'm is %d ears old. %s is good nome" % (name, age, name))
print("Time is:", datetime.datetime.now() - time_now)
"""

