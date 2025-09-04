import random as r


matrix = [[1, 2, 3, 4],
          [5, 6, 7, 8],
          [9, 10, 11, 12],
          [13, 14, 15, 16]]

lst_matrix = []
l_m = len(matrix[0])

for i in range(l_m):
    for j in range(l_m):
        lst_matrix.append(matrix[i][j])

r.shuffle(lst_matrix)
lst_index=0
for i in range(l_m):
    for j in range(l_m):
        matrix[i][j] = lst_matrix[lst_index]
        lst_index += 1


print(matrix)        

