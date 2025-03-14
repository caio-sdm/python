frase = 'Curso em Vídeo Python'
print(frase)
um = frase.count('o')
dois = frase.count('o', 0, 13)
tres = frase[9]
treze = frase[:10]
quatorze = frase[10:]
quatro = frase [9:13]
cinco = frase [:21:2]
seis = frase [7::3]
print(um,dois,tres,treze,quatorze,quatro,cinco,seis)
sete = frase.find(' Py')
nove = frase.find('shask')
print(sete, nove)
oito= 'Vídeo' in frase
dez = 'gsha' in frase
print(oito, dez)
onze = frase.replace('Python', 'PHP')
#para salvar a mudança, definir frase = frase.replace
print(onze)
doze = frase.lower()
frase.split()
print("""fghkijgtdfghjkloiuytfvbnmkiuytgbnmkiuygtv
bnmkiytredfghjklkjhfgdfghjklkjytrsdfghjklkjhgfrdfg
hkijgtdfghjkloiuytfvbnmkiuytgbnmkiuygtvbnmkiytredf
ghjklkjhfgdfghjklkjytrsdfghjklkjhgfrdfghkijgtdfghj""")
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(len(frase))
print(frase.split())
#para mostrar apenas um elemento dessa split, colocar var = frase.split(), depois print(var[1]),
#que mostra o elemento 1, "em". Para mostrar uma letra, colocar o número da divisão e, dentro dela, a letra.
#Ex: print(var[0][2]) mostrará a letra 2 da palavra 0 'Curso', que é 'r'
