def asc_user():
    asc_user_number = input("Enter a number: ")
    if not asc_user_number.isdigit():
        print("Please enter a walid number!!!", end=" ")
        return None
    else:
        return int(asc_user_number)


def check_answer():
    asc_revenge = input("Do you want to play again? (Y/n): ").lower()
    if not asc_revenge.isalpha():
        return None
    elif asc_revenge == "y":
        return True
    else:
        return False


def quiz():
    user_answer = asc_user()  # Store the user's answer in a variable
    victory_number = 47
    if user_answer is not None:  # Check if the user provided a valid number
        if user_answer == victory_number:
            print("You got it right!")
        else:
            print("Your number is WRONG!")


while True:
    quiz()
    play_again = check_answer()
    if play_again is None:
        print("Invalid input. Exiting.")
        break
    elif not play_again:
        print("Goodbye!")
        break
