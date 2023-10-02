# cd lection_10 -> ls
# -- in terminal give output ->
# work_with_file_1.py work_with_file_2.py code_lector encode_decode.py pip.py work_with_file.py

# cd - це скакалка по директоріям

# У пайтон існують два види файлів - текстові (txt) та бінарні (bin, exe, com)

# Потрібно відкрити файл швидко. Бо система його блокує і ішні не мають до нього доступу

f = open("code_lector/welcome.txt", "a")
try:
    # work with file
    f.write("This line is first in the welcome file\n")

finally:  # це відноситься до трай і виконається обовʼязково після всього коду, навіть якщо буде виняток
    f.close()

# ----------------------------------------------------------------

with open("code_lector/welcome.txt", "a") as f:
    f.write("Its a second message in file\n")
    f.read(7)      # read 7 characters but if we opened in (byte mode) we read 7 bytes (it's a lot)
    f.read()       # read full file
    f.readline()   # read first line
    f.readlines()  # read all lines. RETURN A LIST!!!

# (f.) have counter. f.read(7) (This li) and then f.read(5) be (ne is)

# f.read() and f.readline() difference is in how we save data

# В обох випадках файл точно закриється

# ----------------------------------------------------------------


