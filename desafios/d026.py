#programa que leia uma frase e mostre: quantas vezes aparece a letra A,
# em que posição ela aprece a primeira vez e que posição ela aparece pela última vez

print('=' * 30)

print("Contador de letras 'A' (serio mesmo? ok)")

frase = str(input('Escreva a frase: ')).lower().strip()
print('A letra A aparece {} vezes\nA letra apareceu a primeira vez na posição {}\nE a última vez na posição {}'.format(frase.count('a'), frase.find('a')+1, frase.rfind('a')+1))

print('=' * 30)
