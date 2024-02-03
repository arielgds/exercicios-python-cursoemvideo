print('Calculadora de aumento')
nome = str(input('Qual o nome do funcionário? '))
salario = float(input('Qual o salário dele? '))
aumento = 10
if salario >= 1250:
    print('Seu novo  salário é R${:.2f}'.format(salario + (salario/100)*aumento))
else:
    aumento = aumento + 5
    print('Seu novo salário é de R${:.2f}'.format(salario + (salario/100)*aumento))
