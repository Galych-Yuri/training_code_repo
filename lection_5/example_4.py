# ввести число, перевірити що ввели саме число,
# піднести до кубічного це число
# це має бути цикл while з можливістю його закінчити


while True:
    ask_user = input("Enter a number: ")

    # Перевірка чи ввели число.
    if not ask_user.isdigit():
        continue

    print(f"The ** of your {ask_user} number is {int(ask_user)**3}")

    out_of_cycle = input("Do you wanna leave? (Y/n) ").strip().lower()
    if out_of_cycle in ("y",):
        break


