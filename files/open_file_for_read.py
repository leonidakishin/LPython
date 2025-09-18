import random as r
file_name = 'lines.txt'

file = open(file_name, 'r', encoding='utf-8')

lst_file = file.readlines()

print(lst_file[r.randrange(len(lst_file))])
    
file.close()