def prve_cvicenie():
    
    # Zadanie: Medzi kazde pismeno sa vlozi velke X
    # Priklad: kvet -> kXvXeXt
    slovo = input("Zadaj lubovolne slovo: ")
    
    # Slovo premenime na list a do kazdej "medzery" vlozime "X"
    slovo_list = "X".join(list(slovo))

    # Printneme
    print(slovo_list)

#prve_cvicenie()

def druhe_cvicenie():

    # Zadanie: zdvojit kazde pismeno v slove
    # Priklad: kvet -> kkvveett
    slovo = input("Zadaj slovo: ")
    
    # Prazdny string pre nove slovo
    nove_slovo = str()

    # Loopneme cez kazde pismeno
    for pismeno in slovo:
        # Pridame ho dvakrat do "nove_slovo"
        nove_slovo += pismeno*2
    
    # Printneme
    print(nove_slovo)

#druhe_cvicenie()

def tretie_cvicenie():
    
    # Zadanie: Opakuje sa podla toho na akej pozicii sa nachadza
    # Priklad: kvet -> kvveeetttt
    slovo = input("Zadaj slovo: ")

    # Prazdny string pre ukladanie pismen
    nove_slovo = str()

    # Loopneme cez pismena
    for value in range(len(slovo)):

        # Podla pozicie vynasobime pismeno vhodnym poctom
        nove_slovo += slovo[value]*(value+1)
    
    # Printneme
    print(nove_slovo)

tretie_cvicenie()

def stvrte_cvicenie():

    # Zadanie: Kazde druhe pismeno nahradit "X"
    # Priklad: Handlova -> HXnXlXvX
    slovo = input("Zadaj slovo: ")

    # Prazdny string pre ulozenie noveho slova
    nove_slovo_list = list(slovo)

    # Loopneme cez kazde druhe pismenko a nahradime ho "X"kom
    for pismeno in range(1,len(slovo),2):
        nove_slovo_list[pismeno] = "X"
    
    # List premenime na string
    nove_slovo = "".join(nove_slovo_list)

    print(nove_slovo)

stvrte_cvicenie()
