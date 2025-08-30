#Вам доступен список pets, содержащий информацию о собаках и их владельцах. 
# Каждый элемент списка – это кортеж вида (кличка собаки, имя владельца, фамилия владельца, возраст владельца).
#Дополните приведенный ниже код так, чтобы в переменной result хранился словарь, в котором для каждого владельца будут 
# перечислены его собаки. Ключом словаря должен быть кортеж (имя, фамилия, возраст владельца), а значением – список кличек 
# собак (сохранив исходный порядок следования).

pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

tmp_dct = {}
result = {}
for e in pets:
    tmp_dct[e[0]] = (e[1], e[2], e[3])

for k_tmp_dct, v_tmp_dct in tmp_dct.items():
    for k1_tmp_dct, v1_tmp_dct in tmp_dct.items():
        if v_tmp_dct not in result.keys():
            result[v_tmp_dct] = k_tmp_dct
        elif  v_tmp_dct in result.keys() and k_tmp_dct not in result[v_tmp_dct]:
            result[v_tmp_dct] = result[v_tmp_dct] + ' ' + k_tmp_dct


for k, v in result.items():
    result[k] = v.split(' ')


print(result)