#Globalne variability sa pouzivaju na vo funkciach na pouzivanie miesto lokalnych
#Rozdiel medzi lokalnou a globalnou variabilitou

#-> Lokalna
def jeden():
    a = "Jablko"
    def voda():
        a = "Hruska"
    voda()
    print(a)
jeden()
# Nasledujuci program nam returne hodnotu Jablko lebo variabilita vo funkcii voda je lokalna (cize plati len v danej funkcii)
# mozme si to overit aj printnutim danej variability v danej funkcii

#-> Globalna
def dva():
    a = "Jablko"
    def voda():
        global a #tymto zadefinujeme aby variabilita "a" bola globalna a nie lokalna
        a = "Hruska" #nasledne danu variabilitu "a" s hodnotou "jablko" prepiseme na "hruska" 
    voda()
    print(a)
dva()
# Nasledujuci program nam returne hodnotu Hruska lebo sme hodnotu a prepisali v definicii
