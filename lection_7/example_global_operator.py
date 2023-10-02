# Глобальна область видимості функцій

name = "Nom"
print(f"Id name: {id(name)}")


def say_hi():
    def say_lo():
        print(f"Hi, {name} inside say_hi function")
    name = "Bobick"
    print(f"ID_Bobick: {id(name)} inside say_hi function")
    print(f"Hi, {name}")
    say_lo()


# Якщо ми хочемо в середині функції не створювати нову змінну name в її локальній области видимосі, а ми хочемо змінити
# глобальну змінну name, для цього в нас є оператор global. Ми пишемо global name - це ми оголосили що у цій функції
# буде використовуватися змінна name з глобального контексту. Тепер ми в теї записали name = "Jose"
def say_bye():
    global name
    name = "Jose"  # Якщо закоментувати то видасть Bye Nom
    print(f"ID Nom_name inside say_bye() is: {id(name)}")
    print(f"Bye, {name}")


def say_good_morning():
    print(f"ID in say_good_morning() is: {id(name)}")
    print(f"Good morning, {name}")


# Оголошується з самого початку змінна name = "Nom". Код відпрацьовує до global name, означає що ми в області видимості
# функціі використовуюмо глобальне значення name, а далі ми кажемо name = "Jose" і фігично перезаписуємо значення з
# глобальної області видимості name = "Nom". Тож коли ми перезаписали значення, наступна функція бере вже його і юзає.

say_hi()
say_bye()
say_good_morning()
