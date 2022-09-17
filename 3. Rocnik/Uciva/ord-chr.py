# Funkcia chr() a funkcia ord() su built-in python funkcie
# Su si celkom pobodne, robia to iste ale opacne..?

# ++> Funkcia chr()
#   Sluzi na ziskanie unicode charakteru na zaklade daneho integera
#   kazdy unicode charakter ma pridelne ciselko na zaklade, ktoreho
#   sa tak identifikuje. 
#   ( range unicode charakterov je od 0 do 1 114 111 )
#   Napriklad znak "@" ma ciselko "64"

# Tipy:
#   Naraz mozete premenit iba jedno cislo, cize nieco ako chr(1,2,5) nebude fungovat.
#   Cislo mimo range od 0 do 1 114 111 nebudu fungovat, napr chr(-100) vypise chybu.

# Ukazka pouzitia:
def chr_funkcia():
    
    # Zadefinujeme si ciselko 10
    ciselko = 10
    # Premenime ho na charakter pomocou chr()
    charakter = chr(ciselko)
    # Pritneme dany charakter cize
    print('Charakter pod cislom {} predstavuje - {}'.format(ciselko,charakter))

    import random
    # Zadefinujeme si nejake nahodne ciselko od najmensieho mozneho po najvacsie
    ciselko = random.randint(0,1114111)
    # Premenime ho na charakter pomocou chr()
    charakter = chr(ciselko)
    # Pritneme dany charakter cize
    print('Charakter pod cislom {} predstavuje - {}'.format(ciselko,charakter))


# ++> Funkcia ord()
#   Je presny opak funkcie chr(), cize na zaklade zadaneho charakteru nam
#   vrati jeho ciselnu hodnotu.
#   Napriklad ciselko "65" nam vrati hodnotu "A"

# Tip(y):
#   Naraz mozete premenit iba jeden charakter na ciselko, cize nieco ako ord('a','b') alebo ord('ahoj') nebude fungovat.

# Ukazka pouzitia:
def ord_funkcia():

    # Zadefinujeme si nejaky znak
    znak = "!"
    # Premenime ho na ciselko pomocou ord()
    cisleko = ord(znak)
    # Printneme ho
    print('Ciselko pod charakterom {} predstavuje - {}'.format(znak,cisleko))

    # Keby sme chceli premenit napriklad celu vetu na hentie ciselka (alebo jednoducho cele slova)
    # tak to mozeme urobit nasledovne:
    # Zadefinujeme si celu vetu ako string
    veta = "Ahoj, ako sa mas?"
    # Premenime ju na list pomocou funkcie list(), ktora to automaticky rozdeli na pismenka
    veta_list = list(veta)
    # Zadefinujeme prazdny list
    list_cisel = []
    # Loopneme cez veta_list (cize cez pismenka)
    for pismenko in veta_list:
        # Premenime item na ciselko
        ciselko = ord(pismenko)
        # A nasledne ho ulozime do listu
        list_cisel.append(ciselko)
    # Printneme hotovy list
    print('Hotovy ciselny list z vety > {} < vyzera takto:\n{}'.format(veta,list_cisel))

ord_funkcia()


