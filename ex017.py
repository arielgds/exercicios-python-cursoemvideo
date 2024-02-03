import math
catetoOposto = float(input('Qual o tamanho do cateto oposto?'))
catetoAdjacente = float(input('Qual o tamanho do cateto adjacente?'))
hipotenusa = math.hypot(catetoOposto,catetoAdjacente)
print('Os catetos são {}(oposto) e {}(Adjacente). A hipotenusa é {}'.format(catetoOposto, catetoAdjacente,hipotenusa))