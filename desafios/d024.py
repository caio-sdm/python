#criar um programa que leia o nome de uma cidade e diz se ele começa ou não com santo

print("=" * 30)

print("A cidade começa com 'Santo'?")

cid = str(input("Escreva o nome da cidade: ")).lower().strip()
sep = cid.split()
if 'santo' in sep[0]:
    print("Sim")
else:
    print("Não")

print("=" * 30)


#outra resolução
"""
cid = str(input("Escreva o nome da cidade: ")).lower().strip()
print(cid[:5] == 'santo')
"""
