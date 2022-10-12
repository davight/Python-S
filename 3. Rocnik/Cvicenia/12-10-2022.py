def prve_cvicenie():

    # Zadanie:
    # Zapiste nejakych 5+ mien otvorte
    # subor a pritnite ich mena a priezviska
    subor = open('ziaci.txt')

    # List riadkov v subore
    list_ziakov = subor.readlines()

    # Loopneme cez kazdy "rad" v liste
    for rad in list_ziakov:

        # Aktualne rad vyzera nejak takto "text text\n"
        # Teda ho splitneme ho podla medzery
        list_info = rad.split(" ")

        # Meno a priezvisko ziaka
        meno = list_info[0]
        priezvisko = list_info[1]

        # Pritneme vysledok
        print('meno: {} \npriezvisko: {}\n'.format(meno,priezvisko), end="")
    
prve_cvicenie()

def druhe_cvicenie():

    # Zadanie: 
    # Kazdy neparny riadok vypis opacne
    # a kazdy parny riadok normalne

    subor = open('ziaci.txt')

    # List riadkov v subore
    list_ziakov = subor.read().split("\n")

    # Aktualny riadok count
    count = 1
    
    # Loopneme cez kazdy "rad" v liste
    for rad in list_ziakov:
        
        # Kukneme ci je parny
        if count%2 == 0:
            # Je parny, cize ho printneme opacne
            opacny_rad = rad[::-1]
            print(opacny_rad)
        
        # Nie je parny cize neopacne
        else:
            print(rad)
        
        # Pripocitame k hodnote
        count += 1
druhe_cvicenie()

def tretie_cvicenie():

    # Zadanie:
    # (subor ktory obsahuje mena zaikov a velda nich ich znamky)

    subor = open('znamky.txt')

    # List riadkov v subore
    list_ziakov = subor.read().split("\n")

    for rad in list_ziakov:

        # Rozdelime rad podla medzery, a priradime potrebne info do var
        info_list = rad.split()
        meno = info_list[0]
        znamky_list, znamky = list(info_list[1]), 0

        # Loopneme cez znamky
        for str in znamky_list:

            # Pridame k celkovemu poctu znamok
            znamky += int(str)

        priemer = znamky / len(znamky_list)

        print('Ziak {} ma priemer znamok {}'.format(meno,priemer))

tretie_cvicenie()
