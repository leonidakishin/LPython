text = input('Введите текст:\n')
print('Введите "да", если будем шифровать:')
if input().lower() == 'да':
    is_shifr = True
else:
    is_shifr = False

print('Выберете язык. Русский - введите "рус", английский - введите "eng":')
if input().lower() == 'рус':
    is_rus = True
else:
    is_rus = False

print('Введите величину сдвига:')
sdvig = int(input())

rus_alph = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
rus_alph_up = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЬЫЪЭЮЯ'
eng_alph = 'abcdefghijklmnopqrstuvwxyz'
eng_alph_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def char_shifr(char, is_shifr, sdvig, is_rus):
    char_result = ''
    index_char = 0
    index_result = 0
    if is_shifr:
        if is_rus:
            if char in rus_alph:
                index_char = rus_alph.index(char)
                index_result = (index_char + sdvig) % 32
                char_result = rus_alph[index_result]
            elif char in rus_alph_up:
                index_char = rus_alph_up.index(char)
                index_result = (index_char + sdvig) % 32
                char_result = rus_alph_up[index_result]
            else:
                char_result = char
        elif not is_rus:
            if char in eng_alph:
                index_char = eng_alph.index(char)
                index_result = (index_char + sdvig) % 26
                char_result = eng_alph[index_result]
            elif char in eng_alph_up:
                index_char = eng_alph_up.index(char)
                index_result = (index_char + sdvig) % 26
                char_result = eng_alph_up[index_result]
            else:
                char_result = char
    else:
        if is_rus:
            if char in rus_alph:
                index_char = rus_alph.index(char)
                index_result = (index_char - sdvig) % 32
                char_result = rus_alph[index_result]
            elif char in rus_alph_up:
                index_char = rus_alph_up.index(char)
                index_result = (index_char - sdvig) % 32
                char_result = rus_alph_up[index_result]
            else:
                char_result = char
        elif not is_rus:
            if char in eng_alph:
                index_char = eng_alph.index(char)
                index_result = (index_char - sdvig) % 26
                char_result = eng_alph[index_result]
            elif char in eng_alph_up:
                index_char = eng_alph_up.index(char)
                index_result = (index_char - sdvig) % 26
                char_result = eng_alph_up[index_result]
            else:
                char_result = char

    return char_result

text_result = ''

def perebor(alph_length):
    for i in range(alph_length):
        text_result_l = ''
        for c in text:
            text_result_l += char_shifr(c, is_shifr, i, is_rus)

        print(text_result_l)

if sdvig != 0:
    for c in text:
        text_result += char_shifr(c,is_shifr, sdvig, is_rus)

    print(text_result)
else:
    perebor(25)