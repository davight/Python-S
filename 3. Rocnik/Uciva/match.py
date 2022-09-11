# Pre pouzivanie funkcie match je potrebna verzia Pythonu 3.10+
# tato verzia vysla okolo roku 2021.

# Match funkcia sluzi na porovnavanie roznych hodnot a nasledne
# vybratie danej moznosti. Match funkcia moze nahradit niektore
# if, elif funkcie.

# ++> Priklad:

# Zadanie:
#   Na zaklade hodnoty pocasia printneme rozne odpovede.
#   Pri pocasi "Prsi" printneme: "Vezmi dazdnik !"
#   Pri pocasi "Slnecno" printneme: "Vezmi slnecne okuliare !"
#   Pri pocasi "Veterno" printneme: "Vezmi mikinu !" 

# Zadefinujeme si variabilitu pocasie s hodnotou "Prsi"
pocasie = "Prsi"


# -> Prva moznost pomocou IF a ELIF
def prva_moznost(pocasie):
    
    # Pomocou if a elif prejdeme vsetky moznosti ci sa
    # pocasie nerovna danej hodnote a na zaklade toho
    # printneme odpoved.
    if pocasie == "Prsi":
        print("Vezmi dazdnik !")
    elif pocasie == "Slnecno":
        print("Vezmi slnecne okuliare !")
    elif pocasie == "Veterno":
        print("Vezmi mikinu !")


# -> Druha moznost pomocou MATCH
def druha_moznost(pocasie):

    # Pomocou match sa automaticky vyberie spravna moznost
    # a na zaklade nej sa printne vhodna odpoved.
    match pocasie:
        case "Prsi":
            print("Vezmi dazdnik !")
        case "Slnecno":
            print("Vezmi slnecne okuliare !")
        case "Veterno":
            print("Vezmi mikinu !")

#TODO: Dopisat: performance, default case, pros & cons, multiple cases

