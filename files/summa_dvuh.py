file_name = 'nums.txt'

file = open(file_name, 'r', encoding='utf-8')
summa = 0
lst = []
for line in file:
    lst.extend(line.split())

print(sum(map(int, lst)))       
file.close()