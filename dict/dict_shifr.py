#Напишите программу для расшифровки секретного слова методом частотного анализа.
#Формат входных данных
#В первой строке задано зашифрованное слово. Во второй строке задано одно целое число nn – количество букв в словаре. 
# В следующих nn строках записано, сколько раз конкретная буква алфавита встречается в этом слове – <буква>: <частота>.

shifr = input()
dct_temp = dict(input().split(': ') for i in range(int(input())))
for _ in dct_temp:
    dct_chastot = {k: v for v, k in dct_temp.items()}

ras_shifr_ovka = ''
for c in shifr:
    ras_shifr_ovka += dct_chastot[str(shifr.count(c))]


print(ras_shifr_ovka)    

