def prveCvicenie(listCisel):

    # Zadanie:
    #  Vynasob cisla v liste, pokial je
    #  list prazdny printni cislo 1.

    o = 1

    if len(listCisel) == 0:
        # List je prazdny, vypisujeme zakladne cislo, teda 1
        return print(o)

    # List, nie je prazdny ideme cez neho loopovat
    for item in listCisel:
        # Vynasobime to itemom, cez ktory prave prebieha loop
        o *= item

    # Returneme odpoved
    return print(o)


# prveCvicenie( [2, 5] )


def druheCvicenie(zaklList):

    # Zadanie:
    #  Z listu vypiste kazdu druhu poziciu,
    #  zacinajuc na indexe 1.

    return print( zaklList[1::2] )


#druheCvicenie( [1, 2, 3, 4, 5] )

def tretieCvicenie(n):

    # Zadanie:
    # Vypis n mocnin od 1 po n

    mocniny = []

    for item in range(1, n+1):

        mocnina = item ** 2
        mocniny.append( str(mocnina) )

    mocniny = " ".join(mocniny)
    return print(f"Mocniny od 1 po cislo {n} -> {mocniny}")

#n = input("Zadaj cislo! \nCislo: ")
#tretieCvicenie( int(n) )

def stvrteCvicenie(v):

    # Zadanie:
    #  Z n listu vyhod vyskyt vsetkych x prvkov

    try:
        v = int(v)
    except ValueError:
        pass

    z = [ 1, 5, 6, 'g', 'c', 3, "Alex", 1 ]

    upravenyList = [ i for i in z if i != v ]

    return print(f"Zakladny list: {z}\n"
                 f"Vyhadzujem znak: {v}\n"
                 f"Upraveny list: {upravenyList}")

#vyhadzovanie = input("Zadaj znak, alebo ciso, ktore chces vyhodit: ")
#stvrteCvicenie( vyhadzovanie )
