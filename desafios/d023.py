#programa que leia um numero de 0 a 9999 e mostre cada digito separado.
# Ex: numero 1856 >
#1 milhar
#8 centenas
#5 dezenas
#6 unidades

print("="*30)

print("Descrição de número")

num = int(input("Digite um número de 0 a 9999: "))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(u, d, c, m))

print("=" * 30)