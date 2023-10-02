

f = open("code_lector/test.txt")
a = f.read()  # extract all data
f.close()
print(a)  # some text
print(type(a))
# <class 'str'>

print(50 * "-")
# ----------------------------------------------------------------

with open("code_lector/test.txt") as f:
    b = f.readlines()
print(b)
# ['This line is first in the welcome file\n', "It's a second message in file\n",
# 'This is third message in welcome file\n', '\n', 'This line brfore last line\n', "It's a last line"]
print(type(b))
# <class 'list'>

print(50 * "-")
# ----------------------------------------------------------------

f = open("code_lector/test.txt")
try:
    c1 = f.readline()  # have inside method counter
    print(c1)
    print(type(c1))  # <class 'str'>
    c2 = f.readline()
    print(c2)
    print(type(c2))  # <class 'str'>
finally:
    f.close()




