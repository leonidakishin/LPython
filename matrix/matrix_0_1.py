#Программа должна вывести указанную матрицу в соответствии с 
#образцом: разместить единицы на главной и побочной диагоналях, остальные позиции матрицы заполнить нулями.


n = int(input())

matrix = []
for i in range(n):
    matrix.append([0] * n)

for i in range(n):
    for j in range(n):
        if i == j or j == n - i - 1:
            matrix[i][j] = 1

for i in range(n):
    for j in range(n):
        str_aij = str(matrix[i][j])
        print(str_aij.rjust(3), end="")
    print()