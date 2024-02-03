r1 = float(input('Qual o tamanho da primeira reta? '))
r2 = float(input('Qual o tamanho da segunda reta? '))
r3 = float(input('Qual o tamanho da terceira reta? '))
lista = sorted([r1, r2, r3])
if lista[0] + lista[1] > lista[2]:
    print('Juntando as retas {}, {}, {} é possível formar um triângulo!'.format(lista[0],lista[1],lista[2]))
else:
    print('Não é possível fazer um triângulo com as retas {}, {}, {}.'.format(lista[0],lista[1],lista[2]))