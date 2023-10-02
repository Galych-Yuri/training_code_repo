my_pets = ["BonyJa", "ZaYa", "biba", "Boba", "script"]
# my_pets_redacted = []

# За класикою ми візьмемо цикл for, крутимо, апендимо змінене слово. З мар не потрібно самостійно викликати функцію,
# вона викличе її сама під час обробки

my_pets_redacted = list(map(str.title, my_pets))
print(my_pets_redacted)
# ['Bonyja', 'Zaya', 'Biba', 'Boba', 'Script']

my_pets_redacted_lambda = list(map(lambda x: x.title(), my_pets))
print(my_pets_redacted_lambda)  # особливість лямбди полягатиме в тому,
# що треба явно викликати функцію через дужки ()? То шо лямбда - сама не викликається іі потрібно викликати руцями
# ['Bonyja', 'Zaya', 'Biba', 'Boba', 'Script']

lst_float_numbers = [3.32434554645, 4.344354647754, 10.4305945687986, 2.968096830485]

lst_float_redacted = list(map(round, lst_float_numbers, range(1, len(lst_float_numbers)+1)))
print(lst_float_redacted)
# [3.3, 4.34, 10.431, 2.9681] last number changed on 3
# На першій ітерації коли в нас відбудеться розпаковка, функція рендж нам видасть одиницю, у функцію раунд буде прокинуто перший елемент та одиничка разом з ним. Як ми памєятаємо у функції раунд коли прокидується другим елементом число то воно є кількістю знаків після коми. На другій ітерації буде взяте наступне исло зі списку і згенерована функцією рендж двійка



