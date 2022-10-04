def prve_cvicenie():
    
    # Zadanie:
    # Sedi mucha na stene ale v programe, teda my zadame nejaku 
    # samohlasku a nahradia sa vsetky samohlasky nasou zadanou.
    
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
