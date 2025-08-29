# Дополните приведенный ниже код так, чтобы он вывел наиболее часто встречающееся слово строки s.
# Если таких слов несколько, должно быть выведено то, что меньше в лексикографическом порядке.


s = "orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley"

result = {}
st_text = set(s.split())
freq_word = ""
freq_max = 0
for c in st_text:
    if freq_max < s.count(c):
        freq_word = c
        freq_max = s.count(c)
    elif freq_max == s.count(c):
        if c < freq_word:
            freq_word = c


print(freq_word)
