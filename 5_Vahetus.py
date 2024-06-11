# Koostage programm, mis vahetab esimese ja viimase elemendi.
# (teine ​​ja eelviimane jne). Vahetatavate elementide arvu tuleb küsida kasutajalt.
# Algses loendis on vähemalt 2 elementi.

elements = [1, 'Alesha', 3, 4, 5, 6, 7, 8, 9, 'Ilon Mask']

print(elements)
print()
while True:
    count = int(input('Mitu elementi igast loendi lõpust tuleks vahetada?: '))

    if count > len(elements) // 2:
        print("Viga! Arv on liiga suur, maksimaalne võimalik väärtus:", len(elements) // 2)
        print()

    else:
        break

listLen = len(elements)
for i in range(count):
    elements[i], elements[listLen-1-i] = elements[listLen-1-i], elements[i]

print()
print("Muudetud loend: ",elements)
