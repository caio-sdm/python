print('Tabuada')
num = int(input('Digite um número para ver sua tabuada: '))
print('A tabuada do {} é:'.format(num))
if num <10:
    print('='*11)
if 99 >= num >= 10:
    print('='*13)
if num > 99:
    print('='*15)
print('{} x {:>2} = {}'.format(num, 1, num*1))
print('{} x {:>2} = {}'.format(num, 2, num*2))
print('{} x {:>2} = {}'.format(num, 3, num*3))
print('{} x {:>2} = {}'.format(num, 4, num*4))
print('{} x {:>2} = {}'.format(num, 5, num*5))
print('{} x {:>2} = {}'.format(num, 6, num*6))
print('{} x {:>2} = {}'.format(num, 7, num*7))
print('{} x {:>2} = {}'.format(num, 8, num*8))
print('{} x {:>2} = {}'.format(num, 9, num*9))
print('{} x {:>2} = {}'.format(num, 10, num*10))
if num <10:
    print('='*11)
if 99 >= num >= 10:
    print('='*13)
if num > 99:
    print('='*15)
