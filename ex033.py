print('Verificando qual é o maior número!')
n1 = int(input('Qual é o primeiro número? '))
n2 = int(input('Qual é o segundo número? '))
n3 = int(input('Qual é o terceiro número? '))
#if n1<n2 and n1<n3:
#    menor = n1
#if n2<n3 and n2<n1:
#    menor = n2
#if n3<n1 and n3<n2:
#    menor = n3
#if n1>n2 and n1>n3: maior = n1
#if n2>n1 and n2>n3: maior = n2
#if n3>n1 and n3>n2: maior = n3
lista = sorted([n1, n2, n3])

print('O maior número é {} e o menor é {}.'.format(lista[2],lista[0]))