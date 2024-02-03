import math
angulo = float(input('Qual o ângulo para ser medido? '))
seno = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tang = math.tan(math.radians(angulo))
print('O valor do ângulo é {} graus. O seno, cosseno e tangente são {:.2f} {:.2f} {:.2f} respectivamente.'.format(angulo, seno, coss, tang))