nomeCompleto = str(input('Qual seu nome completo? ')).strip()
nomes = nomeCompleto.split()
print('Primeiro nome: {}'.format(nomes[0]))
print('Último nome: {}'.format(nomes[len(nomes)-1]))