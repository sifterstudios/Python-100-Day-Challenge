import os

import day8_art

clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
should_run = True

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def initialize():
    print(day8_art.logo)
    init_direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if init_direction == 'encode' or init_direction == 'decode':
        init_text = input("Type your message:\n").lower()
        init_shift = int(input("Type the shift number:\n"))
        return init_text, init_shift, init_direction
    else:
        clearConsole()
        initialize()


def operate(plain_text, shift_amount, operation):
    shifted_text = ""
    for c in plain_text:
        if c not in alphabet:
            shifted_text += c
        else:
            i = alphabet.index(c)
            i += shift_amount
            if i > alphabet.index('z'):
                i -= alphabet.index('z')
            if i < alphabet.index('a'):
                i += alphabet.index('a')
            shifted_text += alphabet[i]
    print(f'The {operation}d text is {shifted_text}')


while should_run:
    text, shift, direction = initialize()
    shift = shift % 26
    direction.lower()
    if direction == 'encode':
        operate(text, shift, direction)
    elif direction == 'decode':
        operate(text, -shift, direction)
    go_again = input("Type 'yes' if you want to go again. otherwise type 'no'\n").lower()
    if go_again == 'yes':
        clearConsole()
        text, shift, direction = initialize()
    elif go_again == 'no':
        print('Goodbye')
        should_run = False
    else:
        clearConsole()
        print("Could not understand that. Try typing 'yes' or 'no'")
        go_again = input("Type 'yes' if you want to go again. otherwise type 'no'\n")
