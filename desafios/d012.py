print('Calculadora de desconto de produto')
p1 = float(input('Preço do produto: '))
d1 = float(input('Valor do desconto: '))
d2 = d1 /100
df = p1 * d2
pf = p1 - df
print('O valor final, com {}% de desconto, é: {}'.format(d1,pf))


