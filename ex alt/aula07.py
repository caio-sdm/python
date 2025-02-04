nome = input('digite seu nome: ')
print('prazer em te conhecer, {:^10}!'.format(nome))
n1 = int(input('digite um número: '))
n2 = int(input('digite outro vaor: '))
s = n1+n2
m = n1*n2
d = n1/n2
su = n1-n2
ex = n1**n2
print('a soma é {}, o produto é {} e a divisão é {:.2f}'.format(s,m,d))
print('a subtração é {}, a potência é {}'.format(su,ex))

