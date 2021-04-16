from random import randint, choice
from os import system
from ascii_images import *
def read_file():
    with open('../archivos/palabras.txt','r', encoding='utf-8') as f:
        return ([line.replace('\n','') for line in f])

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
        raise ValueError('solo una letra, cabas de perder un intento F')
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
    
def play(chosen_word):
    attempts = 0
    word_list = list(chosen_word)
    chanses=6
    result = ['_' for letter in chosen_word]
    result[0] = word_list[0]
    print(TITLE)
    print(f'intentos Restantes: {chanses}')
    print(HANG_MAN[0])
    print(result)

    while(chanses > attempts):
        try:
            letter = get_one_letter()
            temporal = compare_attempt(letter, word_list)
            if temporal:
                result = join_results(temporal,result)
            else:
                attempts += 1
                print('has perdido un intento')
            print(f'intentos Restantes: {chanses-attempts}')
            print(HANG_MAN[attempts])
            print(result)

        except ValueError as ve:
            print(result)
            print(ve)

    system('clear')
    if(chosen_word == ''.join(result)):
        print(YOU_WON)
    else:
        print(HANG_MAN[len(HANG_MAN)-1])
        print(GAME_OVER)

    print(f'la palabra era "{chosen_word}"')

def run():
    words = read_file()
    chosen_word = chose_word(words)
    play(chosen_word)

if __name__=="__main__":
   run()