#Дана квадратная матрица чисел. Напишите программу, которая зеркально отображает её элементы относительно горизонтальной оси симметрии.

n = int(input())

matrix = [input().split() for _ in range(n)]

x = n // 2

for i in range(x):
    matrix[i], matrix[n - i] = matrix[n - i], matrix[i]

for i in range(n):
    print(*matrix[i])    