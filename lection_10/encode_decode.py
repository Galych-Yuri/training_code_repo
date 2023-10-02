variable = "Fcdsdfwrty567"
print(variable.encode('utf-8'))  # Розкодує?

variable_1 = "Р"
variable_1 = variable_1.encode('utf-8')
print(variable_1)  # b'\xd0\xa0'  Символ
# Б - означає що дані представлено у байтовому вигляді
# Х - означає що закодовано у 16-річній системи вирахунку


artist_bytes = b'Tage \xc3\x85s\xc3\xa9n'
artist = (artist_bytes.decode())
print(artist)  # Tage Åsén

# "Latin1" використовує перші 128 байт АСКІ а решту майже всі букви мов Європи

artist_latin1 = artist.encode("latin1")
print(artist_latin1)  # b'Tage \xc5s\xe9n'
artist_decoded = artist_latin1.decode("latin1")
print(artist_decoded)  # Tage Åsén

# Спочатку енкодуємо у тому кодуванні в якому закодоване,
# а потім декодуємо у те кодування яке нам потрібне

# --------------------------------

data = b'ci\xc3\xa0o'

with open("code_lector/task.txt", "w", encoding="Latin1") as f:
    f.write(data.decode("Latin1"))

# Якщо ми відкриваємо файл з якисось кодуванням, то пушити в нього треба з таким самим кодуваннямм

try:
    f = open("code_lector/task.txt")
    word = f.read()
    print(word)
    print(type(word))
finally:
    f.close()

# utf-8  for Europe lang
# utf-16 for Asian  lang
# but all they're coding in unicode
