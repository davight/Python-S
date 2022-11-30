# Cvicenia z labakov.
# Den - 24.11.2022 ; Skupina - II

# +++> Info:

# - Citanie suborov v pythone je pomerne vyuzivana
#   funkcia. Citanie suborov v pythone je mozne
#   pomocou funkcie open("path_k_suboru"). Funkcia
#   open() obsahuje viacero modov, ktore si mozeme
#   zvolit. Medzi tie zakladne patri mod 'r' ( ktory
#   je zaroven zakladny ) sluzi IBA na citanie suboru,
#   mod 'w', ktory sluzi na PISANIE do suboru.
#   @ Tip:
#     Pre citanie zo suboru pouzivaj built-in funkciu
#     "with open("path") as n", ktora automaticky po
#     jej ukonceni subor zavrie
#
# - Funkcia enumerate je built-in python funkcia, ktora
#   vytvori list s tuples, ktore na prvom indexe obsahuju
#   poradie zakladneho listu a na druhom indexe ich hodnotu.
#   Nasledne mozeme cez tieto hodnoty loopovat naraz.
#   @ Priklad:
#       l = ["Jablko", "Hruska", "Banan"]
#       for index, ovocie in enumerate(l):
#           print(index, ovocie)

# ++ Zadanie k prvemu cviceniu:
#   Napis program, ktory z n surobu vypise
#   vsetky riadky a ich poradove cislo
#   ( Optimalne vedla seba. )
# ++ Obmedzenia:
#   Treba pocitat s tym, ze NEVIEME kolko
#   riadkov sa v subore nachadza.

# Mozne riesenie:
def prvyPriklad():

    with open("C:\\Users\\PC\\Desktop\\cicky.txt") as subor:

        riadky = subor.read().split("\n")

        for cislo, text in enumerate(riadky):
            print(f"{cislo + 1}. {text}")

prvyPriklad()

# ++ Zadanie k druhemu cviceniu:
#   Jedna sa o to iste zadanie ako pri prvej
#   ulohe len s tym, ze vypisujeme subor od konca.
#   Samozrejme cisla riadkov musia sediet!

def druhyPriklad():

    with open("C:\\Users\\PC\\Desktop\\cicky.txt") as subor:

        riadky = subor.read().split("\n")
        obratene = list(enumerate(riadky))[::-1]

        for cislo, text in obratene:
            print(f"{cislo + 1}. {text}")

#druhyPriklad()

# ++ Extra bonusove a extremne hnusne necitatelne zadanie:
#   To iste co druhe cvicenie len s tym, ze vsetko bude
#   v jednom riadku.
# ++ Obmedzenia:
#   Ziadne ";" tam nechcem vidiet.

def nerobteTo():

    with open("C:\\Users\\PC\\Desktop\\cicky.txt") as subor:
        [ print(f"{cislo + 1}. {text}") for cislo, text in list(enumerate(subor.read().split("\n")))[::-1] ]

#nerobteTo()
