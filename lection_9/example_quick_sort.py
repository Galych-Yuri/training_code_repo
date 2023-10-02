# Другий допотопний спосіб сортувати.

def partition(seq, start_index, end_index):
    pivot = start_index

    for i in range(start_index+1, end_index+1):
        if seq[i] < seq[start_index]:
            pivot += 1
            seq[i],  seq[pivot] = seq[pivot], seq[i]
    seq[start_index], seq[pivot] = seq[pivot], seq[start_index]

    return pivot


def quick_sort(seq, start_index, end_index):

    # print(seq)

    if start_index >= end_index:
        return

    pivot = partition(seq, start_index, end_index)
    quick_sort(seq, start_index, pivot - 1)
    quick_sort(seq, pivot + 1, end_index)


sequence = [-100, 3, 45, 76, 33, 23, 10, -345, 343, 15, 12]


print(f"Before sort: {sequence}")

# quick_sort(sequence, 0, len(sequence)-1)

print(f"After sort: {sequence}")



