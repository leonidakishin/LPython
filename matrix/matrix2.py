# На вход программе подаются два натуральных числа n и m – количество строк и столбцов в матрице, затем nn строк по m целых чисел в каждой,
# #отделенных символом пробела.

# Напишите программу, которая находит индексы (строку и столбец) первого вхождения максимального элемента.


n = int(input())
m = int(input())


def read_matrix(n_l):
    matrix_local = []
    for i in range(n_l):
        row = [int(i) for i in input().split()]
        matrix_local.append(row)
    return matrix_local


matrix = read_matrix(n)

max_aij = matrix[0][0]
max_i = 0
max_j = 0

for i in range(n):
    for j in range(m):
        if max_aij < matrix[i][j]:
            max_aij = matrix[i][j]
            max_i = i
            max_j = j

print(max_i, max_j)
print()
for i in range(n):
    print(*matrix[i])
