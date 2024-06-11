# Nikolai mõtles nimekirja põhjal “kasutu” numbri leidmisele.
# Selle olemus on järgmine: see võtab suvalise arvude loendi, leiab neist suurima,
# jagab selle loendi pikkusega ja asendab selle loendis jagamise tulemusega.


def Replace(list):
    maxNum=max(list)
    resault=maxNum/len(list)
    list[list.index(maxNum)]=resault

    
numbers=[3, 4, 75, 332, 65, 23, 34]
print(numbers)

Replace(numbers)
print(numbers)
