# Cvicenie z labakov.
# Den - 2.2.2023; Skupina - II

import math

# +++> Info
#
# - V pythone sa funkcie vytvaraju pomocou def
#   prikazu. Za prikazom uvadzame nas nazov
#   funkcie a zatvorky a dvojbodku.
#   @Priklad:
#       def moja_funkcia():

# - Do funkcii mozeme posuvat nejake informacie
#   ako argumenty. Tie zadavame do zatvoriek pri
#   vytvarani fukcii. Nasledne ich vo funkcii
#   mozeme pouzivat ako lokalne variability.
#   Nasledne musime funkciu volat s poskytnutymi
#   argumentami. ( tiez v zatvorkach )
#   @Priklad:
#       def moja_funkcia(meno, vek):
#           print(f"meno - {meno}")
#           print(f"vek - {vek}")
#       moja_funkcia("Alex", 32)
#       moja_funkcia("Peter", 23)

# - Vo funkciach existuju aj default value parametre
#   to znamena, ze pokial my nezadame nejaku hodnotu
#   bude dosadena ta defaultna. Defaultne parametre
#   sa nastavuju pri vytvarani funkcii v zatvorkach.
#   Syntax je: value = def_value
#   @Priklad:
#       def moja_funkcia(meno, vek = 20)
#           print(f"meno - {meno}")
#           print(f"vek - {vek}")
#       moja_funkcia("Alex", 29)
#       moja_funkcia("Peter")


# ++ Zadanie k prvemu cviceniu:
#   Vytvor funkciu, ktora ako argumenty bude
#   brat cestu k suboru a text, ktory sa do
#   daneho suboru vypise.
# ++ Obmedzenia:
#   Ziadne staticke hodnoty!

# Mozne riesenie:
def prve_cvicenie(path: str, text: str) -> None:
    with open(path, 'w') as file:
        file.write(text)

prve_cvicenie("ahoj.txt", "ahoj filipko")

# ++ Zadanie k druhemu cviceniu:
#   Vytvor funkciu, ktora ako paramter
#   bude brat nejaky integer a returne
#   factorial toho cisla.

# Mozne riesenie:
def druhe_cvicenie(cislo: int):
    for i in range(1, cislo):
        cislo *= i
    return cislo

print(druhe_cvicenie(5))
print(druhe_cvicenie(3))

# ++ Zadanie k tretiemu cviceniu:
#   Vytvor funkciu, ktora ako parameter
#   bude brat nejaky polomoter a volitelne
#   ludolfove cislo pi. A returtni obsah
#   kruznice zo zadanych hodnot.

# Mozne riesenie:
def tretie_cvicenie(r: int, pi=math.pi):
    return pi * (r ** 2)

print(tretie_cvicenie(10))
print(tretie_cvicenie(10, 3.14))

# ++ Zadanie k stvrtemu cviceniu
#   Vytvor funkciu, ktora bude pocitat
#   ludolfovo cislo pi do co najvacsej
#   presnosti kazdu upravu cisla pritni.

# Mozne riesenie:
def stvrte_cvicenie():
    pi, c = 3, 2
    while True:
        pi += 4 / (c*(c+1)*(c+2))
        print(pi)
        pi -= 4 / ((c+2)*(c+3)*(c+4))
        print(pi)
        c += 4

stvrte_cvicenie()
