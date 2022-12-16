# @@@ Ucivo
# Tuples

# - Tuple je zoznam dat, ktore ako v liste
# su zoradene, mozno opakujuce sa ale
# narozdiel od listu su nemenne.
# - Funkcie ako append, remove, yada yada
# pre tuples nefunguju. Tuples nie su robene
# na to aby sme ich po zadefinovani nejak
# menili / upravovali.
# - Tuples na oznacenie pouzivaju oble zatvorky
# narozdiel od listov, ktore pouzivaju
# hranate zatvorky.

# - Pre premenu listu na tuple mozeme pouzit
# built-in funkciu tuple(list).
# - Pre premenu tuple na list mozeme pouzit
# built-in funkciu list(tuple)

def prvyPriklad():

    # Vytvorime si nejaky list, upravime
    # ho a premenime na tuple.

    zoznam_ziakov = ["Alex", "Mario", "Tomas"]
    zoznam_ziakov.append("Marko")

    tuple_ziakov = tuple(zoznam_ziakov)
    print(f"Toto je zoznam ziakov v tuple: {tuple_ziakov}")
    print(type(tuple_ziakov))

prvyPriklad()
