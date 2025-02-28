#sorteio de quatro pessoas, lendo o nome e escrevendo o nome do escolhido

import random

print('sorteador de aluno')
print('='*30)
alunos = 'humberto', 'doisberto', 'tresberto', 'quatroberto'
sorteio = random.sample(alunos, 1)
print(sorteio)
print('='*30)

#jeito mais certo de fazer

#print('sorteador de aluno')
#print('='*30)
#a1 = str(input('nome do primeiro aluno: '))
#a2 = str(input('nome do segundo aluno: '))
#a3 = str(input('nome do terceiro aluno: '))
#a4 = str(input('nome do quarto aluno: '))
#alunos = [a1, a2, a3, a4]
#sorteio = choice(alunos)
#print(sorteio)
#print('='*30)