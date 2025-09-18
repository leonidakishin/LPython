import string
file_name = 'data.txt'
     
with open(file_name, 'r', encoding='utf-8') as file:
    lst = []
    for line in file:
        lst.extend(line.split())
summa = 0
for e in lst:
    for i in range(len(e)):
        ch = ''
        if e[i].isdigit():
            if ch == '': 
                ch += e[i]


print(lst)        

