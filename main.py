from random import choice

from constants import banner, words
from util import get_letter
from hangman import hangman


def main():
    while True:
        print(f'\n\n{banner}\n')
        letter = ' '
        while letter not in 'YN':
            letter = get_letter('Play a game of hangman? (Y/N)')
        if letter == 'Y':
            hangman(choice(words))
            input('Press Enter to continue...')
            continue
        else:
            break


if __name__ == '__main__':
    main()
