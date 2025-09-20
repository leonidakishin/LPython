import string
file_name = 'data.txt'

bukv = 0
slov = 0
strok = 0

with open(file_name, 'r', encoding='utf-8') as file:
    lst = []
    for line in file:
        lst.extend(filter(lambda x: x if x.isalpha() else '',line))
        slov += len(line.split())
        strok += 1    

print('Input file contains:')
print(f'{len(lst)} letters\n{slov} words\n{strok} lines')   