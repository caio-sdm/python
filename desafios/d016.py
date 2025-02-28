#leia um numero real e mostre a porção inteira dele

from math import modf

print('Porção inteira de um número fracionário')
print('='*30)
num = float(input('Escreva o número: '))
d, i = modf(num)
print('A porção inteira de {} é igual a {}'.format(num, i))
print('='*30)

# outros modos de fazer:
# math.trunc(num)
#.format(num, int(num))