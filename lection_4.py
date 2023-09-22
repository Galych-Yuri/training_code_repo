first_name = "Євген"
second_name = "Арефа"
second_name = second_name[-1::-1].title()
print(second_name)  # Афера


# user_first_name, user_second_name = (input("Enter your first name: ").lower(),
#                                      input("Enter your second name: ").lower())
#
# user_first_second_name = input("Enter your first and second name: ").lower()
# user_first_second_name = user_first_second_name.strip()
#
# print(user_first_name.title(), user_second_name.title(), user_first_second_name.title())


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

create_file = open("python.txt", "w")
# w - режим запису (взагалі перезапису, тобто коли відкриє файл в якому
# вже щось є, то воно видалить данні з нього і запише нові)
# а - режим дозапису
print("Hello, world", file=create_file)
create_file.close()  # будьякий файл обовʼязково потрібно закривати після використання,
# бо інакше це зробить прибиральник і дані можуть не дозаписатися, а файл буде заблокований.


