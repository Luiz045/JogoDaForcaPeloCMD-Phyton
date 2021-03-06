def interface(string='', tip='', tries=[], errors=0, win=None):
    def imageErros(errors):
        if errors == 0:
            return '''
                       +---+
                       |   |
                           |
                           |
                           |
                           |
                     =========
                    '''

        if errors == 1:
            return '''
                       +---+
                       |   |
                       O   |
                           |
                           |
                           |
                     =========
                   '''

        if errors == 2:
            return '''
                       +---+
                       |   |
                       O   |
                       |   |
                           |
                           |
                     =========
                   '''

        if errors == 3:
            return '''
                       +---+
                       |   |
                       O   |
                      /|   |
                           |
                           |
                     =========
                   '''

        if errors == 4:
            return '''
                       +---+
                       |   |
                       O   |
                      /|\  |
                           |
                           |
                     =========
                   '''

        if errors == 5:
            return '''
                       +---+
                       |   |
                       O   |
                      /|\  |
                      /    |
                           |
                     =========
                   '''
        if errors == 6:
            return '''
                       +---+
                       |   |
                       O   |
                      /|\  |
                      / \  |
                           |
                     =========
                   '''

    print('\n' * 30)
    print('\033[0;36m=' * 40)
    print('{:^{}}'.format('JOGO DA FORCA', 40))
    print('=' * 40, '\033[0m')

    print(f'Dica: {tip}')
    print('Letras: ', end='')
    for i in tries:
        if i in string:
            print(f'\033[32m{i.upper()}\033[m ', end='')
        else:
            print(f'\033[31m{i.upper()}\033[m ', end='')

    print()
    print(imageErros(errors))

    print(' ', end='')
    for j in string:
        if j in tries:
            print(f' {j.upper()} ', end='')
        else:
            print(' _ ', end='')
            
    print()
    print()
    print('-' * 40)
    if win:
        print('\033[32mPARABENS, VOC?? VENCEU!!!')
        print(f'Voc?? fez {len(tries)} Tentativas, e {errors} estavam erradas.\033[m')
        print('Deseja jogar de novo? [S/N]: ')

    elif win == False:
        print('\033[31mVOC?? PERDEU! :(')
        print('Que pena, voc?? fez 6 tentativas erradas.')
        print(f'A palavra era "{string}"')
        print('Mais sorte na pr??xima!\033[m')
        print('Deseja jogar de novo? [S/N]: ')

    else:
        print(f'\033[32mVoc?? ainda tem {6 - errors} Tentativas!\033[m')
        print('\033[33mEscolha uma letra: \033[m')

