


#Не забывайте, что [].append(one_row)  и [].append(list(one_row)) - это совершенно разный результат выполнения кода 
# (передать ссылку на объект в памяти и создать новый объект в памяти)


str_num = input().split()

n = int(str_num[0])
m = int(str_num[1])

matrix = []
for i in range(n):
    matrix.append([0]*n)
    
temp_row = []
for j in range(m):
    temp_row.append(j+1)
#print(temp_row)

for i in range(n):
    for j in range(m):
        matrix[i][j] = temp_row[j]
    temp_row.append(temp_row.pop(0))

print()
for i in range(n):
    print(matrix[i])