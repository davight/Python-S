def prveCvicenie():

    # Zadanie:
    #  Zistite ci su zadane dve slova anagram.
    #  Teda ci sa slova skladaju z toho druheho
    #  navzajom, napriklad: obb = bob; ahoj = hoja

    slova = input("Zadaj dve slova, oddelene medzerou: ")

    slova = tuple(slova.split())
    #slova = slova.split()

    if len(slova) != 2:
        return print("Neplatny vstup! \nOcakavany pocet slov: 2\nZadany pocet slov: {}".format(len(slova)))

    if sorted(slova[0]) == sorted(slova[1]):
        return print("Je to anagram")

    print("Nie je anagram!")

#prveCvicenie()

def druheCvicenie():

    # Zadanie:
    #  Zisti ci sa nejake prvky v lubovolnom tuple opakuju
    #  ak ano tak ake sa opakuju, kolko je tam tych co sa
    #  opakuju kolkokrat sa opakuju a vypis ich.

    t = (1, 2, 3, 4, 4, 5, 23, 3, 5, 4)
    
    duplicates, count = [], 0

    for item in t:

        if t.count(item) > 1:
            # Opakuje sa
            if item not in duplicates:
                # Este nebol v liste
                duplicates.append(item)
                count += 1
    
    print("Celkom bolo v tuple {} opakovani.".format(count))

    for item in duplicates:

        print("Prvok {} sa opakuje v liste {}krat".format(item, t.count(item)))

druheCvicenie()
    
            


