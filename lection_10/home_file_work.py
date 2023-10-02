(user_input_1,
 user_input_2,
 user_input_3,
 user_input_4) = (input("Enter your text here: "),
                  input("Enter your text here: "),
                  input("Enter your text here: "),
                  input("Enter your text here: "))


with open("code_lector/home_task.txt", "w") as f:
    f.write(user_input_1 + "\n" + user_input_2 + "\n")


with open("code_lector/home_task.txt", "a") as f:
    f.write(user_input_3 + "\n" + user_input_4 + "\n")
