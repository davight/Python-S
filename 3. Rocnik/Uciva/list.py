# funkcie:
# count, find, sort, reverse


# ++> Funkcie append(), extend(), insert()
#  Vsetky tieto tri funkcia maju nieco
#  spolocne a to je rozsirovat list.

# ++> Funkcia append()
#  Funkcia append() pridava do listu prave
#  jeden item a to prave na posledne miesto v
#  liste. Na type dat, ktore vkladame nezalezi.
#  @ Format pisania: list.append([item])

# ++> Funkcia extend()
#  Funkcia extend() pridava (rozsiruje list)
#  do listu vsetky iterable typy dat
#  (t.j. list, tuple, set). Je taktiez mozne
#  rozsirit list stringom, string vlozi ako
#  list charakterov. Item sa vzdy vlozi
#  prave na posledne miesto v liste.
#  @ Format pisania: list.extend([item])

# ++> Funkcia insert()
#  Funkcia insert() je podobna funkcii append()
#  ale hlavny rozdiel je v tom, ze v tejto funkcii
#  musime specifikovat, na ktore miesto item chceme
#  vlozit. 
#  @ Format pisania: list.append([index], [item])


def prikladJeden():

    zakladnyList = [1, 2, 3, 4, 'a', 'b', 'c', "Alex", "Filip", "Marko"]
    print(f"Zakladny list: {zakladnyList}\n")

    # @@@ Vkladanie do listu pomocou append()

    prveVlozenie = zakladnyList.copy()
    #prveVlozenie.append(1)
    print(f"Prva uprava pomocou funkcie append: {prveVlozenie}")

    druheVlozenie = zakladnyList.copy()
    druheVlozenie.append("Mario")
    print(f"Druha uprava pomocou funkcie append: {druheVlozenie}")

    tretieVlozenie = zakladnyList.copy()
    tretieVlozenie.append(["Foo", "Bar"])
    print(f"Tretie uprava pomocou funkcie append: {tretieVlozenie}")
    # Mozeme si vsimnut, ze list, ktory sme vlozili do zakladnehoListu
    # sa vlozil iba ako jeden item.

    # @@@ Vkladanie do listu pomocou extend()

    stvrteVlozenie = zakladnyList.copy()
    stvrteVlozenie.extend(["Foo", "Bar"])
    print(f"Prva uprava pomocou funkcie extend: {stvrteVlozenie}")

    piateVlozenie = zakladnyList.copy()
    piateVlozenie.extend([1, 2])
    print(f"Druha uprava pomocou funkcie extend: {piateVlozenie}")

    siesteVlozenie = zakladnyList.copy()
    siesteVlozenie.extend("AHOJ")
    print(f"Tretia uprava pomocou funkcie extend: {siesteVlozenie}")
    # Mozeme si vsimnut, ze sa string AHOJ vlozil do listu ako
    # list charakterov -> 'A', 'H', 'O', 'J'

    # @@@ Vkladanie do listu pomocou insert()

    siedmeVlozenie = zakladnyList.copy()
    siedmeVlozenie.insert(2, "Cicky")
    print(f"Prva uprava pomocou funkcie insert: {siedmeVlozenie}")

    osmeVlozenie = zakladnyList.copy()
    osmeVlozenie.insert(10, 1)
    print(f"Druha uprava pomocou funkcie insert: {osmeVlozenie}")

    deviateVlozenie = zakladnyList.copy()
    deviateVlozenie.insert(-2, "Macicky")
    print(f"Tretia uprava pomocou funkcie insert: {deviateVlozenie}")

#prikladJeden()

# ++> Funkcia remove()
#  Odstrani prvy vyskyt itemu z listu,
#  pokial tam item nie je vyhodi chybu.
#  @ Format pisania: list.remove([item])

# ++> Funkcia pop()
#  Odstrani z listu item na zaklade pozicie.
#  Pokial nezadas ziadnu poziciu vyhodi prave
#  posledny item z listu. Pokial zadas
#  poziciu mimo rangu listu vyhodi error.
#  @ Format pisania: list.pop(index)
#  + Tip:
#     Indexovanie zacina na 0.

# ++> Funkcia clear()
#  Vycisti list, bude prazdny, empty...
#  Format pisania je: list.clear()

def prikladDva():
    
    zakladnyList = [1, 2, 3, 4, 'q', 'r']
    print(f"Zakladny list: {zakladnyList}\n")

    # @@@ Mazanie pomocou remove()

    prveMazanie = zakladnyList.copy()
    prveMazanie.remove(1)
    print(f"Prva uprava pomocou funkcie remove: {prveMazanie}")

    druheMazanie = zakladnyList.copy()
    druheMazanie.remove('r')
    print(f"Druha uprava pomocou funkcie remove: {druheMazanie}")
    
    # @@@ Mazanie pomocou pop()

    tretieMazanie = zakladnyList.copy()
    tretieMazanie.pop(2)
    print(f"Prva uprava pomocou funkcie pop: {tretieMazanie}")

    stvrteMazanie = zakladnyList.copy()
    stvrteMazanie.pop()
    print(f"Druha uprava pomocou funkcie pop: {stvrteMazanie}")

    # @@@ Mazanie pomocou clear()

    piateMazanie = zakladnyList.copy()
    piateMazanie.clear()
    print(f"Prva uprava pomocou funckei clear: {piateMazanie}")

prikladDva()
