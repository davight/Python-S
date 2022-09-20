# Cvicenia z 20.9.2022 pristupne vdaka Alexovi, @Echnico

def prve_cvicenie():
    
    # 1. Zadaj nejake slovo (alebo vetu)
    # 2. Zadaj nejake pismeno
    # Skontroluj a nasladne vypis ci sa dane pismeno nachadza v slove. (alebo vete)
    # Ak sa tam nachadza tak ho aj spocitaj.
    veta = input("Zadaj nejake slovo, alebo vetu:\n")
    zadane_pismeno = input("Zadaj nejake pismeno, ktore chces najst v tvojej zadanej vete: ")

    # Existuje viacero moznosti pre najdenie daneho pismenka
    # Ukazeme si dve "asi" najjednoduchsie

    def prva_moznost():
        # ++> 1. Moznost 
        #   Loopneme cez kazde pismeno vo vete
        #   A zistime ci sa rovna zadanemu pismenu
        count = 0
        
        for pismeno in veta:
            # Variabilita pismeno predstavuje kazde pismeno z "veta"
            if pismeno == zadane_pismeno:
                count += 1
        
        if count > 0:
            # Pismeno sa tam nachadza!
            return ('Zadane pismeno {} sa vo vete nachadza {}krat!'.format(zadane_pismeno,count))
        # Pismeno sa tam nenachadza ani raz!
        return ('Zadane pismeno {} sa vo vete nenachadza ani raz!'.format(zadane_pismeno))
    
    print(prva_moznost())

    
    def druha_moznost():
        # ++> 2. Moznost
        #   Pomocou funkcie list.count(str)

        count = veta.count(str(zadane_pismeno))
        
        if count > 0:
            # Pismeno sa tam nachadza!
            return ('Zadane pismeno {} sa vo vete nachadza {}krat!'.format(zadane_pismeno,count))
        # Pismeno sa tam nenachadza ani raz!
        return ('Zadane pismeno {} sa vo vete nenachadza ani raz!'.format(zadane_pismeno))
    
    print(druha_moznost())

prve_cvicenie()

def druhe_cvicenie():

    # Zadaj hocijake slovo
    # Printne sa ti ci je slovo rovnake aj ked sa otoci
    # Priklad:
    # - TAHAT printne ANO pretoze slovo "TAHAT" je "TAHAT" aj opacne
    # - ALEX printne NIE pretoze slovo "ALEX" je obratene "XELA"

    slovo = input("Zadaj slovo, ktore chces overit: ")
    slovo_opacne = slovo[::-1]
    
    if slovo_opacne == slovo:
        # Slova su rovnake
        print("Slovo {} je rovnake z oboch stran!".format(slovo))
    else:
        # Nie su rovnake
        print("Slovo {} je z druhej strany {}, cize nie su rovnake!".format(slovo,slovo_opacne))

def tretie_cvicenie():

    # Zadaj rodne cislo s "/" (napr: 030421/6789)
    # Pritne sa rodne cislo bez "/"
    rodne_cislo = input("Zadaj rodne cislo: ")

    # Znova existuje viacero moznosti, ukazem 2 najjednoduchsie


    def prva_moznost():

        # Rodne cislo splitneme podla znaku "/"
        # a printneme vsetky casti.
        # To znamena ze je jedno kde sa "/" nachadza a kolkokrat sa tam nachadza.
        
        # Split na zaklade "/"
        rodne_cislo_list = rodne_cislo.split("/")

        # Spojenie listu
        rodne_cislo_upravene = "".join(rodne_cislo_list)
        
        print("Tvoje rodne cislo {} bolo upravene na {}.".format(rodne_cislo,rodne_cislo_upravene))
    
    prva_moznost()

    def druha_moznost():

        # Tato moznost je viac statickejsia, pretoze ak zadal PLATNE rodne cislo
        # tak ocakvame ze sa znak "/" bude nachadzat na presnej pozicii.

        prva_cast = str(rodne_cislo[:6])
        druha_cast = str(rodne_cislo[7:])

        print("Tvoje rodne cislo {} bolo upravene na {}.".format(rodne_cislo,prva_cast+druha_cast))
    
    druha_moznost()

tretie_cvicenie()