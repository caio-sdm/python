#calculadora de hipotenusa

from math import sqrt, hypot

print('Cálculo de Hipotenusa')
print('='*30)
co = float(input('Escreva o cateto oposto: '))
ca = float(input('Escreva o cateto adjacente: '))
hi = sqrt(co**2 + ca**2)
print('A hipotenusa, quando o cateto oposto é {} e o cateto adjacente é {}, é igual a {}'.format(co,ca,hi))
print('='*30)

# outra forma de fazer
# hi = math.hypot(co, ca)
