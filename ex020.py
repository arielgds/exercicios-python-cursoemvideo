from random import shuffle
aluno1 = str(input('Qual o nome do primeiro aluno? '))
aluno2 = str(input('Qual o nome do segundo aluno? '))
aluno3 = str(input('Qual o nome do terceiro aluno? '))
aluno4 = str(input('Qual o nome do quarto aluno? '))
listaAlunos = [aluno1, aluno2, aluno3, aluno4]
shuffle(listaAlunos)
print('A ordem de apresentação dos alunos vai ser: {}, {}, {}, {}'.format(listaAlunos[0], listaAlunos[1], listaAlunos[2], listaAlunos[3]))