import random
import os
import time

part_zero = [
    '   ',
    '   ',
    '   ',
    '   ',
    '   ',
    '   ',
    '   '
]

part_one = [
    '   ',
    '   ',
    '   ',
    '   ',
    '   ',
    '  /\\',
    ' /  \\'
]

part_two = [
    '    ',
    '   |',
    '   |',
    '   |',
    '   |',
    '  / \\',
    ' /   \\'
]

part_three = [
    '   ____________',
    '   |',
    '   |',
    '   |',
    '   |',
    '  / \\',
    ' /   \\'
]

part_four = [
    '   ____________',
    '   |',
    '   |         0',
    '   |',
    '   |',
    '  / \\',
    ' /   \\'
]

part_five = [
    '   ____________',
    '   |',
    '   |         0',
    '   |         |',
    '   |         |',
    '  / \\',
    ' /   \\'
]

part_six = [
    '   ____________',
    '   |',
    '   |         0',
    '   |         |',
    '   |         |',
    '  / \\       / ',
    ' /   \\'
]

part_seven = [
    '   ____________',
    '   |',
    '   |         0',
    '   |         |',
    '   |         |',
    '  / \\       / \\',
    ' /   \\'
]

part_eight = [
    '   ____________',
    '   |',
    '   |         0',
    '   |        /|',
    '   |         |',
    '  / \\       / \\',
    ' /   \\'
]

part_nine = [
    '   ____________',
    '   |',
    '   |         0',
    '   |        /|\\',
    '   |         |',
    '  / \\       / \\',
    ' /   \\'
]

part_ten = [
    '   ____________',
    '   |         |',
    '   |         0',
    '   |        /|\\',
    '   |         |',
    '  / \\       / \\',
    ' /   \\'
]

drawings = [part_zero, part_one, part_two, part_three, part_four, part_five,
            part_six, part_seven, part_eight, part_nine, part_ten]

countries = ['Russia', 'Germany', 'France', 'Italy', 'Spain', 'Ukraine', 'Poland', 'Romania',
             'Netherlands', 'Belgium', 'Greece', 'Portugal', 'Sweden', 'Hungary', 'Belarus',
             'Austria', 'Serbia', 'Switzerland', 'Bulgaria', 'Denmark', 'Finland', 'Slovakia',
             'Norway', 'Ireland', 'Croatia', 'Moldova', 'Albania', 'Lithuania', 'Slovenia',
             'Latvia', 'Estonia', 'Montenegro', 'Luxembourg', 'Malta', 'Iceland', 'Andorra',
             'Monaco', 'Liechtenstein', 'Gibraltar']


def print_starting_statements():
    print('\n')
    print('     Hello dear player!  \n')
    print('This is a simple game of Hangman.  ')
    print(f'The rules are simple.There are {len(countries)} ')
    print('european countries.Every time the ')
    print('list with them will  shuffle and you')
    print('should guess the right country by ')
    print('guessing each letter.You have  ten')
    print('tries!')


def shuffle_and_pick():
    random.shuffle(countries)
    num = random.randint(0, len(countries) - 1)
    return countries[num]


def pick_rand_letters(wrd):
    lst = list(range(1, len(wrd)))
    choice1 = random.choice(lst)
    return [0, choice1]


def check_for_equal_letters(input_letter, word, guessed):
    added = False
    if input_letter in word:
        ind = word.index(input_letter)
        if ind in guessed:
            try:
                ind = word.index(input_letter, ind+1)
            except ValueError:
                return added, guessed
        guessed.append(ind)
        added = True

    return added, guessed


def get_word(wrd, guessed):
    return ' '.join(['__' if x not in guessed else wrd[x] for x in range(len(wrd))])


def ask_for_input():
    letter = input('Please input only one letter:')
    if len(letter) > 1:
        print('Please only 1 character at a time!')
        return ask_for_input()
    if not letter.isalpha():
        print('Please input only letters!')
        return ask_for_input()
    return letter


def clear():
    os.system('cls') if os.name == 'nt' else os.system('clear')


def play_game():
    clear()
    print_starting_statements()
    global drawings
    word = shuffle_and_pick()
    guessed_indexes = pick_rand_letters(word)
    start_value = 0
    while True:
        if len(guessed_indexes) == len(word):
            print(f'You are victorious! THE WORD IS "{word.upper()}"')
            exit()
        [print(*x, sep='') for x in drawings[start_value]]
        print(get_word(word, guessed_indexes))
        if start_value == 10:
            print(f'You died! The right word is {word}!')
            exit()
        letter = ask_for_input().lower()
        added, guessed_indexes = check_for_equal_letters(letter, word, guessed_indexes)
        if not added:
            print('Sorry, try again next time!')
            start_value += 1
        else:
            print('Right!')
        time.sleep(1.5)
        clear()


play_game()
