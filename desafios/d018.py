#programa que leia um angulo, e mostra o seno, cosseno e tangente

from math import radians, sin, cos, tan
print('Calculadora de seno, cosseno e tangente')
print('='*30)
ang = float(input('Digite o ângulo: '))
sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))
print('O ângulo {}° tem seno igual a {:.3f}, cosseno igual a {:.3f} e tangente igual a {:.3f}'.format(ang,sen,cos,tan))
print('='*30)
