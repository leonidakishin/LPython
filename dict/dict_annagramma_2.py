#На вход программе подаются два предложения. Напишите программу, которая определяет, являются они анаграммами или нет. 
# Ваша программа должна игнорировать регистр символов, знаки препинания и пробелы.


#lst = [word.strip('.,!?:;-') for word in input().lower().split()]
lst1 = [c for c in input().lower() if c not in '.,!?:;- ']
lst2 = [c for c in input().lower() if c not in '.,!?:;- ']

dct1, dct2 = {},{}

for c in lst1:
    dct1[c] = dct1.get(c,0) + 1
for c in lst2:
    dct2[c] = dct2.get(c,0) + 1

if dct1 == dct2:
    print('YES')
else:
    print('NO')    


