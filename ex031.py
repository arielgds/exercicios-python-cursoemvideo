print('=== Viação cidade do aço ===')
print('Bem vindo!')
viagem = float(input('Qual é a distância da viagem? '))
if viagem >= 200:
    print('De acordo com nossas tarifas, a viagem de {}Km custará R${:.2f}.'.format(viagem, (viagem*0.45)))
else:
    print('De acordo com nossas tarifas, a viagem de {}Km custará R${:.2f}.'.format(viagem, (viagem*0.5)))