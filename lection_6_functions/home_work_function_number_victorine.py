# Сделать программу в виде функций в которой нужно будет угадывать число.

def quiz():
    victory_number = 47
    asc_user_number = input("Enter a number: ")

    if not asc_user_number.isdigit():
        print("Your number is invalid! Try again.")
    else:
        user_number = int(asc_user_number)

    if user_number == victory_number:
        print("You god damm right!")
    else:
        print("Your number is WRONG!")


quiz()
