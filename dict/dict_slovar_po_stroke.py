#Дополните приведенный ниже код так, 
#чтобы в переменной result хранился словарь, в котором для каждого символа строки text будет подсчитано количество его вхождений.


text = 'footballcyberpunkextraterritorialityconversationalistblockophthalmoscopicinterdependencemamauserfff'
result = {}
st_text = set(text)
for c in st_text:
    result[c] = text.count(c)

print(result)