# If pouzivame ked potrebujeme aby sa program spraval na zaklade
# zadanych podmienok. 
# Pre splnenie podmienky, podmienka musi vyjst (bool) True (fun fact: ak podmienka vyjde int 1 tak je to to iste ako bool True)
# Pri podmienkach sa da pouzit "and" (kde obe casti musia vyjst True) alebo "or" (kde aspon jedna cast musi byt True)
# If podmienky sa daju skladat pomocou elif (else if) a else 

# Pozor: Pri porovnavani stringov nezabudnite na pouzitie uvodzoviek (a == "Tits")

# Pri podmienkach sa pouzivaju tieto operatory: (pouzivajte bez zatvoriek)
#   (==) porovna ci sa strany rovnaju (ak sa rovnaju vyjde True)
#   (!=) porovna ci sa nerovnaju (ak sa nerovnaju vyjde True)
#   (>) porovna ci je lava strana vacsia ako prava (ak je lava vacsia vyjde True) - funguje len pri variabilitach typu float a int
#   (<) porovna ci je lava strana mensia ako prava (ak je lava mensia vyjde True) - funguje len pri variabilitach typu float a int
#   (>=) porovna ci je lava strana vacsia alebo ROVNA ako prava (ak je lava strana vacsia alebo rovna vyjde True) - funguje len pri variabilitach typu float a int
#   (<=) porovna ci je lava strana mensia alebo ROVNA ako prava (ak je lava strana mensia alebo rovna vyjde True) - funguje len pri variabilitach typu float a int

# -> Prvy priklad:
def jeden():
    a = "Jablko" # Zadeklarujeme variabilitu a typu string s hodnotu "Jablko"
    
    if a == "Jablko": # Vytvorili sme podmienku v ktorej zistujeme ci "a" sa rovna "Jablko"
        print('Je to pravda!') # Podmienka vysla True a printla sa nam veticka
jeden()

# -> Druhy priklad:
def dva(): # + Pouzitie elif a else
    a = "Lulia"
    
    if a == "Jakub": # Porovnali sme, ci "a" sa rovna "Jakub", v tomto pripade vyslo False cize posuvame sa v podmienkach dalej
        print('Je to Jakub')
    
    elif a == "Samo":
        print('Je to Samo') # V tejto elif podmienke sme porovnali ci "a" sa rovna "Samo", v tomto pripade nam vyslo znova False a pokracujeme dalej
    
    else: # Dostali sme sa az k else, pri ktorej sa NEZADAVA ziadna podmienka, je to take "nudzove" vychodisko, ktore sa vyberie pokial sa nevybrala ziadna ina podmienka
        print('Je to niekto iny.. :(')
dva()

# -> Treti priklad:
def tri(): # + Pouzitie "and"
    a = 10
    b = "Palino"

    if a == 10 and b == "Mario": # V tejto podmienke sledujeme ci "a" sa rovna "10" A ZAROVEN ci "b" sa rovna "Mario", co vyslo False pretoze "b" sa rovna "Palino"
        print('Je to tak!')
    
    elif a == 10 and b == "Palino": # V tejto podmienke znova sledujeme to iste ale teraz nam uz vyslo True pretoze "a" sa rovna "10" a ZAROVEN "b" sa rovna "Palino"
        print('Trafili sme to!')
    
    else: # K else sa nedostaneme pretoze predchadzajuca podmienka sa splnila a tento cyklus bol ukonceny
        print('Dnes som este nespal')

# -> Stvrty priklad:
def styri():
    a = 54
    b = "Kevin"

    if a/2 >= 102 and b == "Kevin":         # V tejto podmienke sme porovnali ci "a" deleno 2 je vacsie alebo rovne ako 102 (Co vyslo false) a ZAROVEN ci "b" sa rovna "Kevin" ( co vyslo True 
        print('Prva podmienka vysla true!') # ale cela podmienka nebola True cize sa nic nestalo a pokracujeme na dalsiu podmienku )
    
    elif a+10 == 34 or b == "Peter":        # V tejto podmienke sa nesplnila ani jedna cast, pokracujeme na dalsiu podmienku
        print('Druha podmienka vysla true!')
    
    elif a != 50: # V tejto podmienke sa splnilo ze "a" sa nerovna "50" a po jej splneni vchadzame do novej podmienky
    
        if b == "Alex": # V tejto podmienke sa nesplnilo, ze "b" sa rovna "Alex", prechadzame na dalsiu
            print('Tretia podmienka prva cast vysla true!')
    
        elif b == "Kevin": # V tejto podmienke sa splnilo ze "b" sa rovna "Kevin" cize sa spustil prikaz, ktory je k nej prideleny
            print('Tretia podmienka druha cast vysla true')
    
    else: # K vychodisku sme sa nedostali, pretoze nejaka podmienka splnena bola.
        print('Ziadna podmienka sa nesplnila!')
