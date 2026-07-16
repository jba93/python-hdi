from random import randint

print("### Iniciando o Jogo ###")
random = randint(0, 100)
chute = 0
chances=10
while chute != random:
    chute = input('Chute um numero entre 0 e 100: ')
    if chute.isnumeric():
        chute = int(chute)
        chances = chances-1
        if chute == random:
            print('')
            print('Parabéns, você venceu! O número era {} e você ainda tinha {} chances.'.format(random, chances))
            print('')
            break;
        else:
            print('')
            if chute > random:                
                print('Você errou rude! Dica: é um número menor.')
            else:
                print('Você errou rude! Dica: é um número maior.')            
            print ('Você ainda tem {} chances.'.format(chances))
            print('')
        if chances == 0:
            print('')
            print('Suas chances acabaram, você perdeu! O número era {}.'.format(random))
            print('')
            break;
print("### Fim de Jogo ###")