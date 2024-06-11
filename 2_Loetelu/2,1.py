# Küsi kasutajalt viis nime. Salvesta need loendisse ja kuva tähestikulises järjekorras.
# Kuva eraldi viimati lisatud nimi.

print('Sisestage 5 nime:')

names=[]

for i in range(0,5):
    userInput=input(f'{i+1}) ') 
    names.append(userInput)

print()
print('Nimed tähestikulises järjekorras:')

sortedNames=names.sort()

for i in range(0,5):
    print(f'{i+1}) {names[i]}')
    

print()
print(f'Esmalt lisatud: {names[0]}')
