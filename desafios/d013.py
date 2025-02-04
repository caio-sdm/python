print('Calculadora de aumento de salário')
s1 = float(input('Valor do salário: '))
a1 = float(input('Valor do aumento: '))
a2 = a1 / 100
af = s1 * a2
sf = s1 + af
print('Seu novo salário, com um aumento de {}%, é igual a: {}'.format(a1,sf))
