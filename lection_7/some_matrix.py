# Іноді краще використовувати None замість якогось значення, так буде легше перевіряти. Бо коли ми поставимо, наприклад
# нуль, то він вже буде якимсь значенням і його можно буде порівнювати. Припустимо що в нас у порівнялці будуть числа
# від 100 і вище, а вже є прописаний нуль. Тож при перевірці буже порівняння з нулем який ми вказали і функція поверне
# не те значення на яке ми розраховуємо.


matrix = []


def create_matrix():
    result = []

    def create_line(number_of_elements):
        result = []
        counter = 0

    while counter < number_of_elements:
        value = input(f"Enter {counter} elements matrix string: ").strip()

        if (len(value) == 1 and value.isdigit()) or \
                (len(value) > 1 and value[1:].isdigit() and
                 (value[0].isdigit() or value[0] == '-')):
            result.append(int(value))
        else:
            pass