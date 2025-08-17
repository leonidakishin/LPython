#На вход программе подаются два натуральных числа nn и mm – количество строк и столбцов в матрице. 
#Создайте матрицу mult размером n×m и заполните ее таблицей умножения по формуле mult[i][j] = i * j.

n = int(input())
m = int(input())


matrix = []
for i in range(n):
    row = [0]*m
    matrix.append(row)

for i in range(n):
    for j in range(m):
        matrix[i][j] = i * j


for i in range(n):
    print(*matrix[i])
