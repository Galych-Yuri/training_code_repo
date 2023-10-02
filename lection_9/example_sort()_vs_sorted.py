# Метод сорт повертає Нону бо він змінює інсуючий список. Також він тільки для списків
# А функція сортед свтрорює новий змінений список, та може міняти інші типи полекцій
#

sequence = [-100, 3, 45, 76, 33, 23, 10, -345, 343, 15, 12]
sequence_1 = [-100, 3, 45, 76, 33, 23, 10, -345, 343, 15, 12]

print(sequence)
# [-100, 3, 45, 76, 33, 23, 10, -345, 343, 15, 12]

sequence_3 = sorted(sequence, reverse=False, key=lambda x: x if x > 50 else 0)
print(sequence_3)
# [-100, 3, 45, 33, 23, 10, -345, 15, 12, 76, 343]

sequence_4 = sorted(list(filter(lambda x: x > 0, sequence)), reverse=False)
print(sequence_4, "sequence 4")
# [3, 10, 12, 15, 23, 33, 45, 76, 343]

print(sequence_1.sort(), f"{sequence_1} Sorted list")
# None [-345, -100, 3, 10, 12, 15, 23, 33, 45, 76, 343] Sorted list

