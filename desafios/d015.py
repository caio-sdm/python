print('Aluguel de carros')
print('='*30)
dias = int(input('Quantos dias alugados? '))
v = float(input('Valor da diária: R$ '))
km = float(input('Quantos km rodados? '))
km1 = float(input('Valor do km: R$ '))
p = (dias * v) + (km * km1)
print('Total a pagar: R$ {:.2f}'.format(p))
print('='*30)
