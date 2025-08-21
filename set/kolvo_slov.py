# Напишите программу для определения общего количества различных слов в строке текста.


string = input()
znaki = ".,;:-?!"
#string = "Snowflakes, snowflakes falling down. Snowflakes, covering up the ground. Making a blanket, soft and white. Making a blanket in the night."
string_clear = ""
for c in string:
    if c not in znaki:
        string_clear += c


lst = string_clear.lower().split()

set_from_lst = set(lst)
print(lst)
print(set_from_lst)
print(len(set_from_lst))
