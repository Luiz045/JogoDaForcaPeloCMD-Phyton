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
                print('  VOCÊ JA ESCOLHEU ESSA LETRA.')
            elif not letter.isalpha():
                print('  POR FAVOR, DIGITE SOMENTE LETRAS.')
            elif letter.split() == '':
                print('  POR FAVOR DIGITE UMA LETRA.')
            elif len(letter) > 1:
                print('  POR FAVOR, DIGITE APENAS UMA LETRA.')
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
