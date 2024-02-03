import random
n = random.randint(1, 5)
print('Tente acertar o número que pensei!')
chute: int = int(input('Que número você acha que eu pensei(de 1 a 5)? '))
if n == chute:
    print('Você acertou! pensei no número {}!'.format(n))
else:
    print('Você errou! pensei no número {}'.format(n))