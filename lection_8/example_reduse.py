# Функція редʼюс повертає одиничне значення. Якщо функції мап та фільтер повертають ітератор, якй потрібно
# перетворювати на список чи щось, то редʼюс повертає значення. В неї потрібно прокинути функцію яка обовʼязково
# приймає два значення і вона щось робить з цими значеннями. Другим аргументоп прокидають обєкт ітерації. І може
# бути третій необовʼязковий аргумент: елемент з якого хочемо почати, тобто стартове число. Наприклад якщо
# поставимо 5, то він почше з 5 + 1, потім 6 +

# Якщо не заданий третій елемент, то вона з донора бере перші два елемента і пропускає їх через нашу
# функцію стандарт сам. Вони заходять, сумуються і повертається сума. Далі береться ця сума і береться
# третій елемент і сумується. і так до фінішу.


from functools import reduce

list_of_values = [1, 0, -5, 66, 10, 2]


def standart_sum(a, b):
    return a + b


sum_list_of_values = reduce(standart_sum, list_of_values)
print(sum_list_of_values)  # 74

sum_list_of_values_3element = reduce(standart_sum, list_of_values, 5)
print(sum_list_of_values_3element)  # 79
# Важливо. число 5 при виконанні закидається в стандарт_сам на позицію (а),
# під час наступної ітерації все сума закидується на позицію (а) і так постійно.
 
list_of_values_lambda = reduce(lambda x, y: x+y, list_of_values)
print(list_of_values_lambda)