# funkcie:
# pop, append, extend, remove, count, find, sort, clear, insert, reverse


# ++> Funkcie append(), extend(), insert()
#  Vsetky tieto tri funkcia maju nieco
#  spolocne a to je rozsirovat list.

# ++> Funkcia append()
#  Funkcia append() pridava do listu prave
#  jeden item a to prave na posledne miesto v
#  liste. Na type dat, ktore vkladame nezalezi.

# ++> Funkcia extend()
#  Funkcia extend() pridava (rozsiruje list)
#  do listu vsetky iterable typy dat
#  (t.j. list, tuple, set). Je taktiez mozne
#  rozsirit list stringom, string vlozi ako
#  list charakterov. Item sa vzdy vlozi
#  prave na posledne miesto v liste.

# ++> Funkcia insert()
#  Funkcia insert() je podobna funkcii append()
#  ale hlavny rozdiel je v tom, ze v tejto funkcii
#  musime specifikovat, na ktore miesto item chceme
#  vlozit. Format pisania je: list.append(index, item)
#  Pricom index predstavuje poziciu, na ktoru chceme
#  item vlozit.


def prikladJeden():

    zakladnyList = [1, 2, 3, 4, 'a', 'b', 'c', "Alex", "Filip", "Marko"]
    print(f"Zakladny list: {zakladnyList}\n")

    # @@@ Vkladanie do listu pomocou append()

    prveVlozenie = [1, 2, 3, 4, 'a', 'b', 'c', "Alex", "Filip", "Marko"]
    prveVlozenie.append(1)
    print(f"Prva uprava pomocou funkcie append: {prveVlozenie}")

    druheVlozenie = [1, 2, 3, 4, 'a', 'b', 'c', "Alex", "Filip", "Marko"]
    druheVlozenie.append("Mario")
    print(f"Druha uprava pomocou funkcie append: {druheVlozenie}")

    tretieVlozenie = [1, 2, 3, 4, 'a', 'b', 'c', "Alex", "Filip", "Marko"]
    tretieVlozenie.append(["Foo", "Bar"])
    print(f"Tretie uprava pomocou funkcie append: {tretieVlozenie}")
    # Mozeme si vsimnut, ze list, ktory sme vlozili do zakladnehoListu
    # sa vlozil iba ako jeden item.

    # @@@ Vkladanie do listu pomocou extend()

    stvrteVlozenie = [1, 2, 3, 4, 'a', 'b', 'c', "Alex", "Filip", "Marko"]
    stvrteVlozenie.extend(["Foo", "Bar"])
    print(f"Prva uprava pomocou funkcie extend: {stvrteVlozenie}")

    piateVlozenie = [1, 2, 3, 4, 'a', 'b', 'c', "Alex", "Filip", "Marko"]
    piateVlozenie.extend([1, 2])
    print(f"Druha uprava pomocou funkcie extend: {piateVlozenie}")

    siesteVlozenie = [1, 2, 3, 4, 'a', 'b', 'c', "Alex", "Filip", "Marko"]
    siesteVlozenie.extend("AHOJ")
    print(f"Tretia uprava pomocou funkcie extend: {siesteVlozenie}")
    # Mozeme si vsimnut, ze sa string AHOJ vlozil do listu ako
    # list charakterov -> 'A', 'H', 'O', 'J'

    # @@@ Vkladanie do listu pomocou insert()

    siedmeVlozenie = [1, 2, 3, 4, 'a', 'b', 'c', "Alex", "Filip", "Marko"]
    siedmeVlozenie.insert(2, "Cicky")
    print(f"Prva uprava pomocou funkcie insert: {siedmeVlozenie}")

    osmeVlozenie = [1, 2, 3, 4, 'a', 'b', 'c', "Alex", "Filip", "Marko"]
    osmeVlozenie.insert(10, 1)
    print(f"Druha uprava pomocou funkcie insert: {osmeVlozenie}")

    deviateVlozenie = [1, 2, 3, 4, 'a', 'b', 'c', "Alex", "Filip", "Marko"]
    deviateVlozenie.insert(-2, "Macicky")
    print(f"Tretia uprava pomocou funkcie insert: {deviateVlozenie}")

prikladJeden()

