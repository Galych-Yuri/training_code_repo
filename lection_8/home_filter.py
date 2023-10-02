# При помощи функции filter() из котрежа слов отфильтровать только те, которые являются полиндромами
# (слова которые читаются одинаково в обе стороны), регистр букв не учитывать.


inputdata = ['Страна', 'шалаш', 'Летел', 'вертолёт', 'УЧУ', 'мэм', 'язык']

input_data_palindrome = list(filter(lambda x: x.lower() == x[::-1].lower(), inputdata))

print(inputdata)
print(f"I found {len(input_data_palindrome)} palindromes.\nThere are words: {input_data_palindrome}")
