def prve_cvicenie():
    
    # Zadanie:
    #  Sedi mucha na stene ale v programe, teda my zadame nejaku 
    #  samohlasku a nahradia sa vsetky samohlasky nasou zadanou.
    
    # Lyrics pesnicky, list samohlasok
    pesnicka = "Sedí mucha na stene, na stene, na stene. Sedí mucha na stene, sedí a spí.  Sedí a buvinká potvorka malinká. Sedí mucha na stene, sedí a spí  Sede meche ne stene ne stene ne stene..."
    samohlasky = list("aeiouyáéíóúý")

    # Samohlaska, ktora sa ma nahradit
    nahradit = input("Zadaj samohlasku, ktoru chces nahradit: ")
    
    if nahradit in samohlasky:
        # Vlozil spravnu samohlasku
        for pismenko in samohlasky:
            # Loopneme cez vsetky samohlasky aby sme ich nahradili
            pesnicka = pesnicka.replace(pismenko,nahradit)
        # Pritneme upravenu pesnicku
        print(pesnicka)
    else:
        # Zadane pismenko sa nenachadza v samohlaskach
        print("Zadane pismenko sa nenachadza v samohlaskach.")

prve_cvicenie()

def druhe_cvicenie():

    # Zadanie:
    #  Scitaj ordinalne cisla kazdeho pismena zo zadanej vety / slova
    
    veta = input("Zadaj vetu alebo slovo:")
    count = 0

    # Loopneme cez kazde pismeno vo vete ( Pri loopovani cez string sa loopuje cez kazdy charakter )
    for pismeno in veta:
        # Pripocitame ord cislo do countu
        count += ord(pismeno)
    
    # Printneme vysledok
    print(f"Zadane slovo/veta -> {veta}, ma sucet ordinalneho cisla vsetkych charakterov: {count}")

druhe_cvicenie()

def tretie_cvicenie(): 
    
    # Zadanie:
    #  Nacitaj: "samohlasku - slovo1 - slovo2" nasledne spocitaj
    #  kolkokrat sa "samohlaska" nachadza v "slovo1" a "slovo2".

    pismenko = input("Zadaj samohlasku: ")
    slova = input("Zadaj DVE slova, oddelene medzerou: ")

    # Kukneme ci sa jedna iba o jedno pismenko a ci sa nachadza v samohlaskach
    if not pismenko in "aeiouyáéíóúý" or len(pismenko) != 1:
        # Pismenko sa nenachadza v samohlaskach!
        print("Nezadal si jednu samohlasku alebo sa o samohlasku ani nejedna!")
        return
    
    list_slov = slova.split(" ")

    # Kukneme ci zadal prave dve slova
    if len(list_slov) != 2:
        # Nezadal prave dve slova
        print("Nezadal si prave DVE slova!")
        return

    # Spocitame kolkokrat sa nachadza zadana samohlaska v slovach
    slovo1, slovo2 = list_slov[0], list_slov[1]
    pocet1, pocet2 = slovo1.count(pismenko), slovo2.count(pismenko)
    
    # Printneme vysledok
    print(f"V slove '{slovo1}' sa samohlaska '{pismenko}' nachadza {pocet1}krat! \nV slove '{slovo2}' sa samohlaska '{pismenko}' nachadza {pocet2}krat!")

tretie_cvicenie()
    

