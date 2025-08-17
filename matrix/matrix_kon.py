#На шахматной доске 8×8 стоит конь. Напишите программу, которая отмечает положение коня на доске и все клетки, которые бьет конь. 
# летку, где стоит конь, отметьте английской буквой N, а клетки, которые бьет конь, отметьте символами *, остальные клетки заполните точками.

kletka = input()

kletki = 'abcdefgh'

kon_j = kletki.index(kletka[0]) + 1
kon_i = int(kletka[1])

matrix = [['.']*8 for _ in range(8)]

matrix[kon_i - 1][kon_j - 1] = 'N'

for i in range(8):
    for j in range(8):
        if (abs(i - kon_i + 1) + abs(j - kon_j + 1) == 3) and abs(i - kon_i + 1) != 0 and abs(j - kon_j + 1) != 0:
            matrix[i][j] = '*'


for i in range(4):
    for j in range(8):
        matrix[i][j], matrix[8 - i - 1][j] = matrix[8 - i - 1][j], matrix[i][j] 

for i in range(8):
    print(*matrix[i]) 











