#sortear a ordem de apresentação. ler o nome dos quatro alunos, e mostrar a ordem que foi sorteada

import random

print('sorteio ordem de apresentção')
print('='*30)
alunos = 'humberto', 'doisberto', 'tresberto', 'quatroberto'
sorteio = random.sample(alunos, 4)
print(sorteio)
print('='*30)

#jeito mais certo de fazer

#print('sorteio ordem de apresentação')
#print('='*30)
#a1 = str(input('primeiro aluno: '))
#a2 = str(input('segundo aluno: '))
#a3 = str(input('terceiro aluno: '))
#a4 = str(input('quarto aluno: '))
#alunos = [a1, a2, a3, a4]
#random.shuffle(alunos)
#print(alunos)
#print('='*30)