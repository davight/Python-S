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

#prveCvicenie()

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
        
        l =  [prItem, akItem]
        
        novyTuple += tuple(l),
        
    print(novyTuple)

#druheCvicenie()

def tretieCvicenie():
    
    # Zadanie:
    #  Nacitaj lubovolne slovo, vytvor tuple
    #  s ich poziciami a indexami
    
    listSlovo = list(input("Zadaj slovo:\n"))
    listSlovo.insert(0, 'x')
    
    print( tuple( enumerate( listSlovo ) )[1:] )

#tretieCvicenie()

def stvrteCvicenie():
    
    # Zadanie:
    #  Dva rovnako-velke tuples v jednom tuple
    #  Treba scitat kazdu hodnotu z jednej s
    #  tou druhou a do noveho tuple vypisat ich
    #  vysledok.
    
    tuples = ((1, 2, 2), (3.4, 5.4, 8.9))
    dlzka = len(tuples[0])
    novyTuple = tuple()
    
    for tupleCisla in tuples:
        
        aktDlzka = len(tupleCisla)
        
        if dlzka != aktDlzka:
            # Nie su rovnako dlhe!
            return print("Tuples nie su rovnako dlhe !")
        
        dlzka = aktDlzka
        
        for i in range(dlzka):
            
            scitanie = 0
            for t in tuples:
                print(t)
                hodnota = t[i]
                print(hodnota)
                if isinstance(hodnota, int) or isinstance(hodnota, float):
                    scitanie += hodnota
                    continue
                
                return print("Nejaka hodnota v nejakom tuple nie je integer alebo float!")
        
            novyTuple += scitanie,
            
    print(novyTuple)
    
stvrteCvicenie()
    
