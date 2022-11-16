# Global const
zakladnyList = [1, 2, 3, 4, 'a', 'b', 1, 'c', 2, "Alex", "Filip", 1, "Marko"]
print(f"Zakladny list: {zakladnyList}\n")

# +++> Funkcie append(), extend(), insert()
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
#  @ Format pisania: list.insert([index], [item])

def prikladJeden():

    global zakladnyList

    # @@@ Vkladanie do listu pomocou append()

    prveVlozenie = zakladnyList.copy()
    prveVlozenie.append(1)
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

prikladJeden()

# +++> Funkcie remove(), pop(), clear()
#  Vsetky tieto tri funkcia maju nieco spolocne
#  a to je odstranovat nieco (vsetko) z listu.

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
#  @ Format pisania: list.clear()

def prikladDva():
    
    global zakladnyList

    # @@@ Mazanie pomocou remove()

    prveMazanie = zakladnyList.copy()
    prveMazanie.remove(1)
    print(f"Prva uprava pomocou funkcie remove: {prveMazanie}")

    druheMazanie = zakladnyList.copy()
    druheMazanie.remove('b')
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

# +++> Funkcie count(), index()
#  Tieto dve funkcie maju spolocne to,
#  ze hladaju / pocitaju nieco v liste.

# ++> Funkcia count()
#  Spocita vyskyt zadaneho itemu v liste.
#  @ Format pisania: list.count([item])

# ++> Funkcia index()
#  Vyhlada a returne prvu poziciu zadaneho
#  itemu v liste. Je mozne specifikovat
#  aj start a end position, znamenajuc,
#  ze bude hladat od start position po
#  end position (exkluzive). Pokial sa
#  dany item v liste nenachdza funkcia
#  returne -1 poziciu.
#  @ Format pisania: list.index([item], start, end)

def prikladTri():

    global zakladnyList

    # @@@ Pocitanie vyskytov pomocou count()

    prvePocitanie = zakladnyList.count("Marko")
    print(f"Prve pocitanie pomocou funkcie count: {prvePocitanie}")

    druhePocitanie = zakladnyList.count(22667121)
    print(f"Druhe pocitanie pomocou funkcie count: {druhePocitanie}")

    # @@@ Hladanie pomocou funkcie pomocou find()

    prveHladanie = zakladnyList.index('a')
    print(f"Prve hladanie indexu pomocou funkcie index: {prveHladanie}")

    druheHladanie = zakladnyList.index(1, 3)
    print(f"Druhe hladanie indexu pomocou funkcie index: {druheHladanie}")

    tretieHladanie = zakladnyList.index(1, 3, -2)
    print(f"Tretie hladanie indexu pomocou funkcie index: {tretieHladanie}")

prikladTri()

# +++> Funkcie reverse(), sort()

# ++> Funkcia reverse()
#  Returne otoceny list.
#  @ Format pisania: list.reverse()

# ++> Funkcia sort()
#  Zoradi list. Pokial list obsahuje
#  iba cisla zoradi ich vzostupne.
#  ( Od najmensieho po najvacsie )
#  Pokial list obsahuje stringy zoradi
#  ich abecedne podla ich prvych pismen.
#  Ak ich chceme zoradit ale opacne,
#  teda zostupne a opak abecedneho mozeme
#  pouzit "reverse=True" argument priamo
#  v sort funkcii.
#  @ Format pisania: list.sort(reverse=True)

def prikladStyri():

    global zakladnyList

    # @@@ Reversnutie listu pomocou reverse()

    zakladnyList.reverse()
    print(f"Prve otocenie listu: {zakladnyList}")

    # @@@ Sortovanie listu pomocou sort()

    listCisel = [1, 2, 54, 53, 10, 1423, 1998, 203]

    listCisel.sort()
    print(f"Prve zoradanie listu cisel: {listCisel}")

    listCisel.sort( reverse=True )
    print(f"Druhe zoradenie listu cisel: {listCisel}")

    listStringov = ['A', 'B', "Alex", "Mario", "Marko", "Jakub", "Filip"]

    listStringov.sort()
    print(f"Prve zoradenie listu stringov: {listStringov}")

    listStringov.sort( reverse=True )
    print(f"Druhe zoradenie listu stringov: {listStringov}")

prikladStyri()
