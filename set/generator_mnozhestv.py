# Используя генератор множеств, дополните приведенный ниже код так, чтобы получить множество, содержащее уникальные слова (в нижнем регистре) строки sentence.
# Результат вывести на одной строке в алфавитном порядке, разделяя элементы одним символом пробела.
sentence = """My very photogenic mother died in a freak accident (picnic, lightning) when I was three, and, save for a pocket of warmth in the darkest past, nothing of her subsists within the hollows and dells of memory, over which, if you can still stand my style (I am writing under observation), the sun of my infancy had set: surely, you all know those redolent remnants of day suspended, with the midges, about some hedge in bloom or suddenly entered and traversed by the rambler, at the bottom of a hill, in the summer dusk; a furry warmth, golden midges."""


lst = [e for e in sentence if e.isalpha() or e == " "]
string = "".join(lst)

st = {e.lower() for e in string.split() if len(e) < 4}

print(*sorted(st))

# ДРУГОЕ РЕШЕНИЕ
unique_words = {el.strip(" :,.!?();") for el in sentence.lower().split()}
print(*sorted(unique_words))

# ЕЩЕ РЕШЕНИЕ
print(
    *sorted(
        ({"".join([j for j in i if j.isalpha()]).lower() for i in sentence.split()})
    )
)

# words = sentence.lower().replace('.', '').replace(',', '').split()
# Или так можно почистить от знаков препинания
