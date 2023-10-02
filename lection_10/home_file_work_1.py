
with open("code_lector/home_task.txt") as f:
    # data = f.read()
    data_lst = f.readlines()

data_lst_without_newline = [line.strip() for line in data_lst]

print(data_lst)
print(data_lst_without_newline)


