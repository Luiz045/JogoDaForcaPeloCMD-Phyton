from random import randint
from Interface import interface
from words import words

#Inicia o jogo em loop.
while True:

    #Define a palavra da rodada.
    rand = randint(0, len(words) - 1)
    string = words[rand]['word'].upper()
    tip = words[rand]['tip'].upper()
    errors = 0
    tries = list()
    win = None

    #Inicia a rodada.
    while True:
        acerts = 0
        interface(string, tip, tries, errors)

        #Verifica se a letra inserida é valida.
        while True:
            letter = input('').upper()
            if letter in tries:
                print('\033[31mVOCÊ JA ESCOLHEU ESSA LETRA.\033[m')
            elif not letter.isalpha():
                print('\033[31mPOR FAVOR, DIGITE SOMENTE LETRAS.\033[m')
            elif letter.split() == '':
                print('\033[31mPOR FAVOR DIGITE UMA LETRA.\033[m')
            elif len(letter) > 1:
                print('\033[31mPOR FAVOR, DIGITE APENAS UMA LETRA.\033[m')
            elif letter.isalpha():
                break

        #Atualiza as variaveis da rodada.
        tries.append(letter)
        for i in string:
            if i in tries:
                acerts += 1

        if letter not in string:
            errors += 1

        if errors == 6:
            win = False
            break

        if acerts == len(string):
            win = True
            break
    
    #Verifica se o jogador ganhou ou perdeu, e se ele quer jogar de novo.
    if win:
        interface(string, tip, tries, errors, win=True)
    
    else:
        interface(string, tip, tries, errors, win=False)

    if input('').upper() == 'N':
        break
