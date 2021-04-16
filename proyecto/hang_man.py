from random import randint, choice
from os import system
from ascii_images import *

def read_words_description():
    with open('../archivos/words_and_meanings.txt','r', encoding='utf-8') as f:
        return [line.strip().split('|',1) for line in f]

def read_file():
    with open('../archivos/palabras.txt','r', encoding='utf-8') as f:
        return ([line.replace('\n','') for line in f])

def chose_word_meanig(words):
    word,meanig = choice(words)
    return (word.lower(),meanig.lower())

def chose_word(words):
    return choice(words).lower()

def compare_attempt(letter, word_list):
    result = []
    letter_exists_in_word = False
    for word_letter in word_list:
        if letter == word_letter:
            result.append(letter)
            letter_exists_in_word = True
        else:
            result.append('_')

    if not letter_exists_in_word:
        return False
    else:
        return result

def get_one_letter():
    letter = input(': ')
    if len(letter) > 1:
        raise ValueError('solo una letra, cabas de perder 2 intentos F')
    else:
        system('clear')
        return letter.lower()

def join_results(new_result, old_result):
    joined_result = []
    for i in range(len(new_result)):
        if new_result[i] != '_':
            joined_result.append(new_result[i])
        elif old_result[i] != '_':
            joined_result.append(old_result[i])
        else:
            joined_result.append('_')
    return joined_result

def play(chosen_word,meaning):
    attempts = 0
    asserts = 1
    word_list = list(chosen_word)
    len_word = len(word_list)
    chanses=6
    result = ['_' for letter in chosen_word]
    result[0] = word_list[0]
    won= False
    while(chanses > attempts and not won):
        try:
            print(TITLE)
            print(f'intentos Restantes: {chanses-attempts}')
            print(HANG_MAN[attempts])
            print(meaning)
            print(result)

            letter = get_one_letter()
            temporal = compare_attempt(letter, word_list)
            if temporal:
                result = join_results(temporal,result)
                won= chosen_word == ''.join(result)
            else:
                attempts += 1

        except ValueError as ve:
            attempts += 2
            system('clear')
            print(ve)

    system('clear')

    if(won):
        print(YOU_WON)
    else:
        print(HANG_MAN[len(HANG_MAN)-1])
        print(GAME_OVER)

    print(f'la palabra era "{chosen_word}"')

def run():
    words = read_words_description()
    option = '1'
    while(option == '1'):
        chosen_word,meaning = chose_word_meanig(words)
        play(chosen_word,meaning)
        option= input('''
        Jugar de nuevo? 1.-Si 0.-No
        ''')
        system('clear')
if __name__=="__main__":
   run()