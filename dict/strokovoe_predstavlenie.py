#Напишите программу, которая будет превращать натуральное число в строку, заменяя все цифры в числе на слова:

dct_cifr = {'0': 'zero', '1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6' :'six', '7' :'seven', '8': 'eight', '9' :'nine'}

str_int = input()
res = ''
for c in str_int:
    res+= dct_cifr[c] + ' '

print(res)