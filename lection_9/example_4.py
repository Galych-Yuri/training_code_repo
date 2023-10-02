list_of_tuples = [
    ("biba", 12),
    ("boba", 12),
    ("script", 8),
    ("zayavr", 13),
    ("bonya", 7),
    ("bonya", 7)
]

print(sorted(list_of_tuples))
# by 1-rst value
# [('biba', 12), ('boba', 12), ('bonya', 7), ('bonya', 7), ('script', 8), ('zayavr', 13)]

print(sorted(list_of_tuples, key=lambda x: x[1]))
# by 2-nd value
# [('bonya', 7), ('bonya', 7), ('script', 8), ('biba', 12), ('boba', 12), ('zayavr', 13)]

print(sorted(list_of_tuples, key=lambda x: (x[1], x[0])))
# by second value and alphabet if same
# [('bonya', 7), ('bonya', 7), ('script', 8), ('biba', 12), ('boba', 12), ('zayavr', 13)]


