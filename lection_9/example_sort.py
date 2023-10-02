# buble Перший допотопний посіб сортувавти
# Порівнює два сусідніх значення і якщо що міняє місцями


def buble_sort(seq):
    for i in range(len(seq) - 1, 0, -1):
        no_swap = True
        for j in range(0, i):
            if seq[j + 1] < seq[j]:
                seq[j], seq[j + 1] = seq[j + 1], seq[j]
                no_swap = False
        if no_swap:
            return


sequence = [-100, 3, 45, 76, 33, 23, 10, -345, 343, 15, 12]

(buble_sort(sequence))
print(sequence)
# [-345, -100, 3, 10, 12, 15, 23, 33, 45, 76, 343]
