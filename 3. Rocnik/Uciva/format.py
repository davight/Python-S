# Funkcia format() je built-in python funkcia pre lepsie formatovanie
# stringov, ktore je vacsinou vyuzivane nasledne v printovani hodnot.

# Vyuzitie:
#   Komplexnejsie, citatelnejsie doplnanie placeholderov do stringov

# ++ Priklad:
#  Chceme printnut Janko si kupil keksik za 0.35€,
#  predavacke dal 0.50€ a ona mu vydala 0.15€. 

def priklad():
    
    # Prva moznost bez pouzitia funkcie format()
    cena_keksiku = 0.35
    ciastka = 0.50 # To je tych 50 centov co jej dal, neviem jak sa to vola
    vydavok = ciastka - cena_keksiku

    print("Janko dal predavacke",ciastka,"€ a ona mu vydala sumu",vydavok,"€")
    # Tato veta sa printne nasledovne:
    # "Janko dal predavacke 0.5 € a ona mu vydala sumu 0.15000000000000002 €"
    # Lenze ako si mozeme vsimnut medzi cislom a znakom € je medzera, ktoru nechceme
    # Teda miesto oddelenia variability ciarkou ju spojime, nie?

    print("Janko dal predavacke",ciastka+"€ a ona mu vydala sumu",vydavok+"€")
    # Pri pokuse o printnuti tohto na nas vyskoci error ze nemozeme scitovat
    # typ float a typ string. Tym padom mozeme pouzit funkciu str() a premenit
    # to na string, nie? 
    # ( Pre otestovanie tej vety musite odstranit predchadzajucu vetu )

    print("Janko dal predavacke",str(ciastka)+"€ a ona mu vydala sumu",str(vydavok)+"€")
    # Tento pokus nam sice vyjde alee je to taka zbytocna obchadzka
    # ked jednoducho mozeme pouzit funkciu format() nasledovne:

    print("Janko dal predavacke {}€ a ona mu vydala sumu {}€".format(ciastka,vydavok))
    # Alebo nasledovneee, kde vymenime poradie

    print("Janko dal predavacke {1}€ a ona mu vydala sumu {0}€".format(vydavok,ciastka))
    # Aleboo nasledovne, kde to hodime do docasnych variabilit
    
    print("Janko dal predavacke {a}€ a ona mu vydala sumu {b}€".format(a=vydavok,b=ciastka))
    # Alebo nasledovnee, kde to automaticky naformatujeme
    
    print(f"Janko dal predavacke {ciastka}€ a ona mu vydala sumu {vydavok}€")


priklad()
