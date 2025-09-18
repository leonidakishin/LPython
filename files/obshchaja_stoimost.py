file_name = 'prices.txt'

file = open(file_name, 'r', encoding='utf-8')
summa = 0
lst = []
for line in file:
    lst.append(line.split('\t'))

for i in range(len(lst)):
    summa += lst[i][1] + lst[i][2]

print(summa)
file.close()