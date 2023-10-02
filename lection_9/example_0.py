# don't use global variables in functions

def same(n):
    for i in range(0, n):
        new_lst.append(i)


new_lst = []
print(same(5), new_lst)
# this is the bad version


def same_1(n):
    new_lst_1 = []
    for i in range(0, n):
        new_lst_1.append(i)
    return new_lst_1
# this is the good version

