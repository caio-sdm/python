#criar um programa que leia o nome completo de uma pessoa e mostre: tudo maiusculo, tudo minusculo,
#quantas letras no total, sem espaço e quantas letras tem o primeiro nome

print("=" * 30)
print("Informações do seu nome")

nome = str(input("Digite seu nome completo: ")).strip()

print('Seu nome em maiúsculas: {}'.format(nome.upper()))
print('Seu nome em minúsculas: {}'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
#print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))

print("=" * 30)
