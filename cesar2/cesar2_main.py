text = input()
eng_alph = 'abcdefghijklmnopqrstuvwxyz'
eng_alph_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def char_shifr(char, sdvig):
    char_result = ''
    index_char = 0
    index_result = 0
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


    return char_result

tmp_text = ''
text_result_tmp = ''
text_result = ''
i = 0
for c in text:
    i += 1
    if (c in eng_alph) or (c in eng_alph_up):
        tmp_text += c

    if (c not in eng_alph) and (c not in eng_alph_up) and tmp_text != '':
        for c1 in tmp_text:
            text_result_tmp += char_shifr(c1,len(tmp_text))
        text_result += text_result_tmp
        text_result += c
        text_result_tmp = ''
        tmp_text = ''
    elif tmp_text == '':
        text_result += c
    elif i == len(text) and tmp_text != '':
        for c1 in tmp_text:
            text_result_tmp += char_shifr(c1,len(tmp_text))
        text_result += text_result_tmp
        text_result_tmp = ''
        tmp_text = ''


print(text_result)