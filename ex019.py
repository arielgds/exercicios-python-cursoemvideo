import random
alunos = ['Chico', 'Francis', 'Léo', 'João', 'Gustavo']
print('Dentro da sala temos alunos: {}, {}, {}, {}, {}. O que vai apagar o quadro agora vai ser o {}'.format(alunos[0], alunos[1], alunos[2], alunos[3], alunos[4], random.choice(alunos)))
