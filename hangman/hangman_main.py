from random import *

lst_words = ['сало','дерево','виноград','конфета','шоколад','дом','крыша','лавочка','мир','свинец','корабль','кошка',
             'парафин','мыло','сон','ветка','лодка','мороженое','одуванчик','рыба','грабли','солнце','вишня','свекла',
             'парашют','картина','воля','цапля','ферзь','бак','небо','море','снег'
            ,'верблюд','ватрушка','пирожок','валенок','лист','паровоз','новость','кран']

def get_word():
    return choice(lst_words).upper()

# функция получения текущего состояния
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

turn_a = True # режим игры с перой и последней буквой

def play(word):
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    flg_guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    if turn_a:
        word_completion = word[0] + word_completion[1:]
        word_completion = word_completion[:len(word_completion) - 1] + word[-1]


    user_input = ''

    print('Игра "Мертвый питон!"\nЯ загадал слово, попробуй угадай!')


    while not flg_guessed:
        print(display_hangman(tries))
        print(word_completion)
        if tries == 0:
            print(f'У вас осталось {tries} попыток! Вы не угадали слово {word}!')
            break
        print('Назови любую букву или назови слово:')
        user_input = input().upper()
        if not user_input.isalpha():
            print(f'Неверный ввод. Попробуйте снова! Осталось {tries} попыток!')
            continue
        if len(user_input) == 1:
            if user_input in guessed_letters:
                print(f'Вы уже называли такую букву! Осталось {tries} попыток! ')
                continue
            elif user_input in word:
                guessed_letters.append(user_input)

                for i in range(len(word)):
                    if word[i] == user_input:
                        word_completion = word_completion[:i] + user_input + word_completion[i+1:]

                if word_completion == word:
                    print(word_completion)
                    print('Поздравляем, вы угадали слово! Вы победили!')
                    flg_guessed = True
                    continue
                else:
                    print(f'Вы угадали букву! Осталось {tries} попыток!')
                    #tries -= 1
                    continue
            else:
                tries -= 1
                guessed_letters.append(user_input)
                print(f'Вы не угадали букву! Осталось {tries} попыток!')
                continue
        elif user_input == word:
            print(word)
            print('Поздравляем, вы угадали слово! Вы победили!')
            flg_guessed = True
            continue
        elif user_input != word:
            if user_input in guessed_words:
                print(f'Вы уже называли слово {user_input}. Осталось {tries} попыток!')
            else:
                tries -= 1
                guessed_words.append(user_input)
                print(f'Вы не угадали слово! Осталось {tries} попыток!')
                continue

flg_game = True

while flg_game:
    print('\nСыграем в "Мертвый питон"? ДА/НЕТ')
    game_start = input()
    if game_start.upper() == 'ДА':
        word = get_word()
    #print(word)
        play(word)
    #play('ДЕРЕВО')
    #print(get_word())
    else:
        print('Ну вот(. Тогда пока!')
        break