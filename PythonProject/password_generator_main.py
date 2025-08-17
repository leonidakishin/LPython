from random import *

digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$&*+-=?@^_'

char = ''
char_tmp = ''

print('Введите количество паролей для генерации:')
count_pass = int(input())
print('Ведите длину одного пароля:')
pass_length = int(input())
print('Включать ли цифры 0123456789? Введите "да" или "нет".')
if input().lower() == 'да':
    is_digits = True
else:
    is_digits = False

print('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? Введите "да" или "нет".')
if input().lower() == 'да':
    is_upper = True
else:
    is_upper = False
print('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? Введите "да" или "нет".')
if input().lower() == 'да':
    is_lower = True
else:
    is_lower = False
print('Включать ли символы !#$%&*+-=?@^_? Введите "да" или "нет".')
if input().lower() == 'да':
    is_punct = True
else:
    is_punct = False
print('Исключать ли неоднозначные символы il1Lo0O? Введите "да" или "нет".')
if input().lower() == 'да':
    is_amb = False
else:
    is_amb = True

if is_digits:
    if is_amb:
        char += digits
    else:
        char += digits[2:]

if is_upper:
    if is_amb:
        char += uppercase_letters
    else:
        char_tmp = uppercase_letters.replace('L','')
        char_tmp = char_tmp.replace('O', '')
        char += char_tmp
        char_tmp = ''

if is_lower:
    if is_amb:
        char += lowercase_letters
    else:
        char_tmp = lowercase_letters.replace('i','')
        char_tmp = char_tmp.replace('l', '')
        char_tmp = char_tmp.replace('o', '')
        char += char_tmp
        char_tmp = ''

if is_punct:
    char += punctuation


def generate_password(length_pass, chars_pass):
    password = ''
    for j in range(length_pass):
        password += choice(chars_pass)
    return password

for i in range(count_pass):
   print(generate_password(pass_length, char))









