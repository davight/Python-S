# While pouzivame vtedy, ked nevieme kedy sa dany cyklus ukonci
# Cyklus while bezi pokial je podmienka splnenia (ak nezadame inak)
# inak povedane pokial je jej vysledok (bool) True

# -> Prvy priklad:
def jeden():
    a = 10 # Zadeklarujeme si variabilitu (int) 10
    while a < 20: # Vytvarame podmienku: Pokial je "a" mensie ako hodnota "20" opakuj toto...
        print('Stale je to mensie!')
        a += 1 # K variabilite "a" pridavame "1"
jeden()

# -> Druhy priklad:
def dva():
    while True: # Vytvarame podmienku, ktora bezi neustale pretoze... True je vzdy True..?
        print('aaaaaa') # Do terminalu sa nam bude neustale printovat "aaaaaaa"
                        # Nezabudnime ze pokial je dana podmienka nekonecna tak dalsie funcie nebudu pokracovat
                        # preto nekonecne loopy nie su odporucane
#dva() # - Pre testovanie inych prikladov zakomentujte tuto funkciu

# -> Treti priklad:
# Pouzitie "and" alebo "or"
# Pri "and" musia byt vsetky podmienky True
def tri():
    a = "Tomas"
    b = 10
    while a == "Tomas" and b > 5: # Pokial sa "a" rovna "Tomas" a ZAROVEN je "b" vacsie ako "5" ..opakuj toto....
        print('Stale je to true !')
        b -= 1 #Od hodnoty odoberame cislo 1. Po dosiahnuti cisla 4 bude loop ukonceny
                #pretoze sme zadefinovali ze obe hodnoty musia byt true..
tri()

# -> Stvrty priklad:
# Pouzitie "and" alebo "or"
# Pri "or" staci ak je jedna podmienka True
def styri():
    a = "Lulia"
    b = 20
    while a == "Alex" or b == 20: # Pokial sa "a" rovna "Alex" ALEBO pokial "b" sa rovna "20" ..opakuj toto....
        print('Stale sa opakujemeee.....')
        b -= 1 # Od hodnoty odoberieme cislo 1. Teda "b" sa uz nadalej nebude rovnat
               #"20", tym padom nebude splnena ziadna podmienka a loop bude ukonceny..
styri()

