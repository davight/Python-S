def prve_cvicenie():

    # Zadanie:
    # Vypiste pocet riadkov v subore

    # Otvorime subor a vsetky riadky ulozime do listu
    subor = open('data.txt')
    list = subor.readlines()

    # Vypiseme dlzku listu, cize pocet riadkov
    print(len(list))

#prve_cvicenie()

def druhe_cvicenie():
    
    # Zadanie:
    # Z jedneho riadku prepisat vsetky riadky
    # do dalsieho, noveho suboru. Pomocou fukcie
    # readline(), nie read() ani readlines().

    # Otvorenie suborov
    starySubor = open('data.txt')
    novySubor = open('nove_data.txt','a')

    # Loopneme cez kazdy riadok v starom subore
    riadok = starySubor.readline()
    while riadok != "":
        
        # Zapisovanie do noveho
        novySubor.write(riadok)

        riadok = starySubor.readline()
    
    # Zatvorenie suborov
    starySubor.close()
    novySubor.close()

#druhe_cvicenie()

def tretie_cvicenie():

    # Zadanie:
    # Znova prekopirujeme cely subor
    # ale kazdy riadok bude dvakrat.

    # Otvorenie suborov
    starySubor = open('data.txt')
    novySubor = open('najnovsie_data.txt','a')

    # Loopneme cez kazdy riadok v starom subore
    riadok = starySubor.readline()
    while riadok != "":
        
        # Zapisovanie do noveho
        novySubor.write(riadok)
        novySubor.write(riadok)

        riadok = starySubor.readline()
    
    # Zatvorenie suborov
    starySubor.close()
    novySubor.close()

#tretie_cvicenie()

def stvrte_cvicenie():

    # Zadanie:
    # Mame dva subory: cisla.txt ; pismenka.txt
    # A my ich chceme vlastne skombinovat.

    list = []

    # Otvorime subory a ich kontent vlozime do listu
    cisla = open('cisla.txt')
    list.extend(cisla.read())

    pismeno = open('pismena.txt')
    list.extend(pismeno.read())

    # Subor, do ktoreho budeme vkladat vysledok
    skombinovane = open('skombinovane.txt','a')

    # Loopneme cez kazdu hodnotu v liste
    for item in list:
        
        # Zapiseme ju do skombinovacieho suboru
        skombinovane.write(item)

#stvrte_cvicenie()

def piate_cvicenie():

    # Zadanie:
    # Mame dva subory: cisla.txt ; pismenka.txt
    # A my ich chceme vlastne skombinovat.

    # Otvorime subory a ich kontent vlozime do listu
    cisla = open('cisla.txt').read().split("\n")

    pismena = open('pismena.txt').read().split("\n")

    # Subor, do ktoreho budeme vkladat vysledok
    skombinovane = open('skombinovane2.txt','a')

    # Loopneme cez kazdu hodnotu v liste
    for item in range(max([len(cisla), len(pismena)])):
        
        # Zapiseme ju do skombinovacieho suboru
        try:
            skombinovane.write(cisla[item]+"\n")
        except:
            pass
        try:
            skombinovane.write(pismena[item]+"\n")
        except:
            pass

#piate_cvicenie()
