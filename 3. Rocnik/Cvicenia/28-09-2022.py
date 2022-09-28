def prve_cvicenie():
    
    # Zadanie: Medzi kazde pismeno sa vlozi velke X
    # Priklad: kvet -> kXvXeXt
    slovo = input("Zadaj lubovolne slovo: ")
    
    # Slovo premenime na list a do kazdej "medzery" vlozime "X"
    nove_slovo = "X".join(list(slovo))

    # Printneme
    print("Nove slovo je: {}".format(nove_slovo))

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
    print("Nove slovo je: {}".format(nove_slovo))

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
    print("Nove slovo je: {}".format(nove_slovo))

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

    print("Nove slovo je: {}".format(nove_slovo))

stvrte_cvicenie()

def piate_cvicenie():

    # Zadanie: Zoberte nejaku vetu, rozdelteju ju na x casti po troch pismenach
    # a tie otocte.
    # Priklad: JETOZAKODOVANYTEXT -> jotazedokavotyntxe
    
    veta = input("Zadaj nejaku vetu: \n")
    veta_spojenie = "".join(veta.split(" "))
    
    # Prazdny list pre novu vetu
    nova_veta = []

    # Loopneme cez kazde tretie pismenko
    for pismenko in range(0, len(veta_spojenie), 3):
        
        # Ulozime si ich
        tri_pismena = veta_spojenie[pismenko:pismenko+3]
        # A pridame do novej vetz
        nova_veta.append(tri_pismena[::-1])

    # Printneme novu, upravenu vetu
    nova_veta = "".join(nova_veta)
    print("Zakodovana veta je: {}".format(nova_veta))

piate_cvicenie()    
