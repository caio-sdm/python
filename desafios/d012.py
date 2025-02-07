print('Calculadora de desconto de produto')
p1 = float(input('Preço do produto: R$ '))
d1 = float(input('Valor do desconto (porcentagem): '))
pf = p1 - (p1 * d1/100)
print('O valor final, com {}% de desconto, é: {:.2f}'.format(d1,pf))


