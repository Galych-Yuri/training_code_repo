user_input = input("Enter a number: ")

"""
if not user_input.isdigit() == 0 то not переверне це значення на False і буде перевірятися умова в or. тобто якщо
(user_input) неможливо привести до (int), то воно переводиться в True і умова виконується. А коли перша умова буде
цифрою, то (nоt) переведе у False і тоді почнеться друга перевірка після (or)
"""
if not user_input.isdigit() or int(user_input) <= 0:
    print("Wrong input!")
elif int(user_input) <= 12:
    print("Orange")
# identical - int(user_input) < or int(user_input) < 18: AND VE CAN int(user_input) < 18 - because we checked <=12
elif 12 < int(user_input) < 18:
    print("CocaCola")
else:
    print("Beer")
