"""
Написати програму, яка отримає ім'я і вік користувача, перевіряє вік і видає вітальне повідомлення залежно від віку:
- менше нуля або нуль, або нуль, або не число: "Помилка, повторіть введення";
- більше нуля до 10 не включно: "Привіт, шкет #Ім'я#";
- від 10 до 18 включно: "Як життя #Ім'я#?"
- більше 18 і менше 100: "Що бажаєте #Ім'я#?"
- в іншому разі: "#Ім'я#, ви брешете - у наш час стільки не живуть..."
Програму необхідно загорнути у вічний цикл.
Після чергового відпрацювання коду, запитувати у користувача "Бажаєте вийти? (Д/Y)".
Якщо відповідь буде буква "Д" або буква "Y" у будь-якому регістрі, то здійснити вихід із вічного циклу.
В іншому разі продовжити виконання програми заново.
----------------------------------------------------------------
"""

while True:

    user_name, user_age = (input("Hi! Enter your name: "),
                           input("And enter your age: "))
    print("Thanks. Loading is start.")

    user_name = user_name.title().strip()

    if user_name.isdigit():
        print(f"Oops your name is strange. Retrying...")
        continue

    if not user_age.isdigit() or int(user_age) <= 0:
        print(f"Error. {user_age} is wrong data!\n     Try again;)")
        continue
    elif int(user_age.isalpha()) < 10:
        print(f"Hi, toddler {user_name}!")
    elif int(user_age) <= 18:
        print(f"How are you doing {user_name}?")
    elif int(user_age) < 100:
        print(f"Can I help you {user_name}?")
    else:
        print(f"{user_name}, you are lying, people dont live so long.")

    quit_check = input("Do you want to quit? (Д/Y): ").lower().strip()
    if quit_check == ("д", "y"):
        break
    else:
        continue

# Mentor answer

while True:

    name = input("Введіть ваше ім'я: ").title()
    age = input("Введіть ваш вік: ")

    if age.isalpha() or int(age) == 0 or not name.isalpha():
        print("Помилка, повторіть введення", sep="\n")
        continue
    elif int(age) < 10:
        print(f"Привіт, шкет {name}")
    elif int(age) <= 18:
        print(f"Як справи, {name}?")
    elif int(age) < 100:
        print(f"Що бажаєте {name}?")
    else:
        print(f"{name}, ви брешете - у наш час стільки не живуть...")

    answer = input("Бажаєте вийти? (Д/Y)").lower()
    if answer in ("y", "д"):
        break
