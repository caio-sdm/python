# programa que leia o nome completo de uma pessoa e mostre o primeiro e o último nome.
# Ex: luis inacio da silva bolsonaro. primeiro nome: luis ; último nome: bolsonaro

print('='*30)

print('Seu primeiro e último nome')

nome = str(input("Escreva seu nome completo: ")).title().strip()
separa = nome.split()
print('Seu primeiro nome é {} e seu último nome é {}'.format(separa[0], separa[-1]))