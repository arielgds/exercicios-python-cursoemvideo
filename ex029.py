print('===== Polícia Rodoviária Federal =====')
velocidade = float(input('Qual a velocidade do seu carro? '))
if velocidade > 80.0:
    print('LIMITE ULTRAPASSADO!')
    print('Sua multa é de R${:.2f}! '.format((velocidade-80)*7))
else: print('Dentro dos limites de velocidade!')