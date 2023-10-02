

def analyze_number(user_input_number):
    if user_input_number.isdigit():
        number = int(user_input_number)
        if number > 0:
            return f"Ви ввели додатнє ціле число: {number}"
        elif number < 0:
            return f"Ви ввели від'ємне ціле число: {number}"
        else:
            return "Ви ввели нуль"
    else:
        try:
            number = float(user_input_number.replace(",", "."))
            if number > 0:
                return f"Ви ввели додатнє дробове число: {number}"
            elif number < 0:
                return f"Ви ввели від'ємне дробове число: {number}"
            else:
                return "Ви ввели нуль"
        except ValueError:
            return f"Ви ввели некоректне число: {user_input_number}"


while True:
    user_input = input("Введіть число або 'вихід', щоб вийти: ").strip().lower()
    if user_input in ["вихід", "exit", "quit", "e", "q"]:
        break
    else:
        print(analyze_number(user_input))
