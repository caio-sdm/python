n1 = float(input('Digite um numero: '))
n2 = float(input('Digite otro numero: '))
so = n1 + n2
su = n1 - n2
v = n1 * n2
d = n1 / n2
print('Entre os números {} e {}: a soma é {}, a subtração é {}, a multiplicação é {} e a divisão é {}'.format(n1, n2, so,su,v,d))

str01 = input('Escreva algo: ')
print('O tipo primitivo desse "algo" é: ', type(str01))
print('É composto apenas por espaços? ', str01.isspace())
print('É uma palavra? ', str01.isalpha())
print('É um número? ', str01.isnumeric())
print('É alfanumérico? ',str01.isalnum())
print('Está em letras minúsculas? ',str01.islower())
print('Está em letras maiúsculas? ',str01.isupper())
print('Está capitalizada? ', str01.istitle())
