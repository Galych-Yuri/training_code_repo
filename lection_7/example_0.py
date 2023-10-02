
a = 0
b = 5

while a < 10:
    a += 1
    if a < b:
        print("a < b")
    elif a > b:
        print("a > b")
    else:
        print("a == b == {0}".format(a))
        break
else:
    print("a != b, a = {0}".format(a))
