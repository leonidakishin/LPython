#На вход программе подается строка текста. Напишите программу, которая выводит слово, которое встречается реже всего, без учета регистра.
#Если таких слов несколько, выведите то, которое меньше в лексикографическом порядке.

text = 'I bought two books: a new book and an old book. The new book was more expensive than the old book.' #input().lower()
znaki = ".,!?:;-"
string_clear = ""
for c in text:
    if c not in znaki:
        string_clear += c

set_from_lst = set(string_clear.lower().split())
lst = string_clear.lower().split()

freq_word = ''
freq_max = 1000
for c in lst:
    
    if lst.count(c) < freq_max:
        
        freq_word = c
        freq_max = lst.count(c)
        
    elif lst.count(c) == freq_max:
       
        if c < freq_word:
           
            freq_word = c

print(freq_word)