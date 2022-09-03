# For cyklus pouzivame pokial vieme kolkokrat chceme danu vec opakovat
# v nasom pripade sme sa zatial ucili iba for cyklus s range


# -> Prvy priklad - Jeden parameter
def jeden():
    for i in range( 10 ): # Vstupujeme do cyklu, ktory sa bude opakovat 10krat a pripocitavat sa pre hodnotu "i"
        print('Opakujem to uz:',i,'krat') # Kazdym prechodom sa "i" zvacsi o 1
        print('komarkomarkomarkomar')
jeden()


# -> Druhy priklad - Dva parametre
def dva():
    for i in range( 5, 10 ): # Pri range mozeme nastavovat viac parametrov >> prvy parameter je zacinajuca hodnota (inclusive - nvm ako to je slovensky)
        print(i) #                                                      >> druhy parameter je konecna hodnota (exclusive - nvm ako to je slovensky) 
dva()
# Cize to znamena ze v tomto cykle sme isli od cisla 5 do cisla 10 (9)
# V parametroch idu pouzivat aj variability, POZOR! da sa doplnat iba integer


# -> Treti priklad - Tri parametre
def tri():
    a = 23
    for i in range( a, a*2, 2 ): # Pri range mozeme nastavovat aj treti parameter, tzv. step. Sluzi na nastavenie kroku, lepsie sa to ukaze ako vysvetluje
        print(i)
tri()
# V tomto cykle sa zacina od cisla "23" ide sa po cislo "46" a po hodnote "2"
