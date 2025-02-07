print('Calculadora de tinta de parede')
alt = float(input('Digite a altura da parede, em metros: '))
com = float(input('Digite o comprimeto da parede, em metros: '))
ar = alt * com
print('A área da parede é igual a {}m²'.format(ar))
lp = int(input('Digite o rendimento da tinta (quantos m² 1 litro pinta): '))
lit = ar / lp
print('A quantidade de tinta necessária para pintar a parede, em litros, é igual a: {}'.format(lit))