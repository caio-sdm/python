print('Calculadora de dólares')
r = float(input('Digite o valor em reais: '))
d = r / 5.77
print('Com R${:.2f}, você teria US${:.2f} dólares'.format(r,d))
