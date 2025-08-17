# На вход программе подаются два натуральных числа n и m. Напишите программу, которая создает матрицу размером n×m
# и заполняет ее числами от 1 до n⋅m в соответствии с образцом.

str_num = input().split()

n = int(str_num[0])
m = int(str_num[1])

matrix = []
temp_row = []
for j in range(m):
    temp_row.append(j+1)
#print(temp_row)
matrix = []

for i in range(n):
    for j in range(m):
        matrix[i][j] = temp_row[j]
    temp_row.append(temp_row.pop(0))




print()
for i in range(n):
    print(matrix[i])
