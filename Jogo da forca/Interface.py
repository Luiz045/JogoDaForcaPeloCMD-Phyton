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
    print(' ','=' * 40)
    print('{:^{}}'.format('JOGO DA FORCA', 42))
    print(' ','=' * 40)

    print(f'  Dica: {tip}')
    print('  Letras:', end=' ')
    for i in tries:
        print(i.upper(), end=' ')

    print()
    print(imageErros(errors))

    print('    ', end='')
    for j in string:
        if j in tries:
            print(j.upper(), end=' ')
        else:
            print('_', end=' ')
            
    print()
    print()
    print(' ','-' * 40)
    if win:
        print('  PARABENS, VOCÊ VENCEU!!!')
        print(f'  Você fez {len(tries)} Tentativas, e {errors} estavam erradas.')
        print()
        print('  Deseja jogar de novo? [S/N]: ')

    elif win == False:
        print('  VOCÊ PERDEU! :(')
        print('  Que pena, você fez 6 tentativas erradas.')
        print(f'  A palavra era "{string}"')
        print('  Mais sorte na próxima!')
        print()
        print('  Deseja jogar de novo? [S/N]: ')

    else:
        print(f'  Você ainda tem {6 - errors} Tentativas!')
        print()
        print('  Escolha uma letra: ')

