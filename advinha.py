from random import randint

print("#### ---------- Vamos jogar? ---------- ####")
min = 0
max = 100
random = randint(min,max)
chute = 0 
chances = 10

while chute != random:
    chute = input(f'Chute um número de {min} a {max}\n')
    if chute.isnumeric():
        chute = int(chute)
        chances = chances - 1
        if chute == random:
            print('\0/\0/\0/\0/\0/\0/\0/\0/\0/\0/\0/\0/\0/\0/')
            print('Parabéns, você venceu! O número era {} e você ainda tinha {} chances.]'.format(random,chances))
            print('\0/\0/\0/\0/\0/\0/\0/\0/\0/\0/\0/\0/\0/\0/')
            break
        else:
            print('')
            if chute > random:
                print('Você Errou!!! Dica: é um número menor!')
            else:
                print('Você Errou!!! Dica: é um número maior!')
                print('Você ainda possui {} chances.'.format(chances))
                print('')
        if chances == 0:
            print('')
            print('Suas chances acabaram! Você perdeu!')
            break
    else:
        print('O que você digitou não é um número!')
print("#### ---------- GAME OVER ---------- ####")