# Postiindex
# Eestis koosnevad postiindeksid 5 numbrist, millest esimene number tähistab maakonda:

# • 1 – Tallinn
# • 2 – Narva, Narva-Jõesuu
# • 3 – Kohtla-Järve
# • 4 – Ida-Virumaa, Lääne-Virumaa, Jõgevamaa
# • 5 – Tartu linn
# • 6 – Tartumaa, Põlvamaa, Võrumaa, Valgamaa
# • 7 – Viljandimaa, Järvamaa, Harjumaa, Raplamaa
# • 8 – Pärnumaa
# • 9 – Läänemaa, Hiiumaa, Saaremaa
# Kirjuta programm, mis kontrollib sisestatud indeksit (tähemärkide arv, vastav andmetüüp jne) ja näitab, millisesse maakonda see kuulub.
# Ja kui sihtnumbriks on Narva, Tallinn ja Kohtla-Järve, siis teavita kasutajat “Püsi kodus!”, muudel juhtudel “Kanna maske!”

regions =['', 'Tallinn', 'Narva, Narva-Jõesuu', 'Kohtla-Järve', 'Ida-Virumaa, Lääne-Virumaa, Jõgevamaa',
           'Tartu linn', 'Tartumaa, Põlvamaa, Võrumaa, Valgamaa', 'Viljandimaa, Järvamaa, Harjumaa, Raplamaa',
           'Pärnumaa', 'Läänemaa, Hiiumaa, Saaremaa']

while True:
    index=input('Sisestage posttiindeks: ')

    if len(index)==5 and index.isdigit() and index[0]!='0' :
        break
    else:
        print('Viga! Ebakoreektne indeks')

firstDigit = index[0] 
firstDigit = int(firstDigit) 

region=regions[firstDigit]

print()
print(f'Teie maakond: {region}')

if firstDigit in [1,2,3]:
    print('Püsi kodus!')
else:
    print('Kanna maske!')


