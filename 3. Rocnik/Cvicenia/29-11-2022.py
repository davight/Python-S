def prveCvicenie():
    
    # Zadanie:
    #  Vlozit z tuple iba elementy vybraneho typu
    #  do noveho tuple, ktory na konci vypiseme.
    # Obmedzenia:
    #  Nesmies pouzit list.
    
    zakladnyTuple = (3, 4, 5, 3.4, "Ahoj", 'C', [1, 2])
    novyTuple = tuple()
    
    for i in zakladnyTuple:
        if isinstance(i, int):
            novyTuple += i,
    
    print(novyTuple)

prveCvicenie()

def druheCvicenie():
    
    # Zadanie:
    #  Usporaduvanie po divnych dvojiciach.
    # Priklad:
    #  tuple = (1, 2, 3, 4)
    #  printne -> ((1, 2), (2, 3), (3,4))
    
    zakladnyTuple = (3, 'B', 6, "Alex")
    novyTuple = tuple()
    
    for index in range( 1, len( zakladnyTuple ) ):
        
        prItem, akItem = zakladnyTuple[index - 1], zakladnyTuple[index]
        tempList = [prItem, akItem]
        
        novyTuple += tuple(tempList),
        
    print(novyTuple)

druheCvicenie()

def tretieCvicenie():
    
    # Zadanie:
    #  Nacitaj nejake slovo, vytvor tuple, ktore obsahuje
    #  tuples, na ktorych je na prvej pozici poradie
    #  pismena a na druhej samotne pismeno.
    # Obmedzenia:
    #  Pozicia zacne na 1

    listSlovo = list(input("Zadaj slovo:\n"))
    listSlovo.insert(0, 'x')
    
    print(
        tuple(enumerate(listSlovo))[1:]
           )

tretieCvicenie()

def stvrteCvicenie():
    
    # Zadanie:
    #  Mas N rovnako-velkych tuple v jednom velkom tuple.
    #  Treba scitat kazdu hodnotu z Ktej pozicie z kazdeho tuple
    #  a ich vysledok vlozit do noveho tuple.

    zoznamTuples = ((1, 2, 3), (3.4, 5.4, 8.9), (1, 1, 1))
    dlzka = len(zoznamTuples[0])
    
    for aktTuple in zoznamTuples:
        
        aktDlzka = len(aktTuple)

        if dlzka != aktDlzka:
            # Nie su rovnako dlhe!
            return print("Tuples nie su rovnako dlhe !")


        dlzka = aktDlzka

    novyTuple = tuple()

    for index in range(dlzka):
            
        count = 0
        for aktTuple in zoznamTuples:

            # Hodnota predstavuje aktualne hodnotu,
            # cez ktoru prechadzame v aktualnom tuple.
            hodnota = aktTuple[index]

            if isinstance(hodnota, int) or isinstance(hodnota, float):
                count += hodnota
            else:
                return print(f"Hodnota '{hodnota}' v tuple {aktTuple} nie je float alebo integer!")
        
        novyTuple += count,
            
    print(novyTuple)
    
stvrteCvicenie()
    
