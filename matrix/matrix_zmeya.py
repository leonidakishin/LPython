# На вход программе подаются два натуральных числа nn и mm. #
# Напишите программу, которая создает матрицу размером n×m, заполнив ее "змейкой" в соответствии с образцом.


n, m = [int(i) for i in input().split()]

matrix = []
temp_row = []
for j in range(m):
    temp_row.append(j + 1)


for i in range(n):
    for j in range(m):
        temp_row[j] = i*m + j + 1
    if i % 2 == 0:
        matrix.append(list(temp_row))
    else:
        matrix.append(list(temp_row[::-1]))

for i in range(n):
    for j in range(m):
        str_aij = str(matrix[i][j])
        print(str_aij.rjust(3), end="")
    print()
