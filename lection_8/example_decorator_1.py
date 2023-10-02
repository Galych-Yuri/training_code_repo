# Burn my ass

def some_global_fun(word="cadabra"):
    def under_fun(default="yep"):
        return default.upper() + "!"

    def under_another_fun(default="yep"):
        return default.lower() + "!"

    if word == "cadabra":
        return under_fun
    else:
        return under_another_fun


some_fun = some_global_fun()

print(some_fun())  # YEP!
print(some_fun("givi"))  # GIVI!

print(some_global_fun()("givi"))  # GIVI!
print(some_global_fun("")("givi"))  # givi!
print(some_global_fun("some text to accssess under_another func")("boba"))  # boba!

# Коротше з глобальній області видимості
# дістати з локальної області видимості
  