n = int(input())

matrix = []

lst = [i for i in range(n)]

for i in range(n):
    if i == 0:
        matrix.append(list(lst))
    else:
        lst =  lst[:n]
        lst.insert(0,i)
        matrix.append(list(lst))

for i in range(n):
    for j in range(n):
        str_aij = str(matrix[i][j])
        print(str_aij.rjust(3), end="")
    print()
