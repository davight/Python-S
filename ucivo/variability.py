# Typy variabilit , spajanie a ich premienanie
# V pythone existuje dost typov ale my si zopakujeme iba jednoduche 4
# Medzi, ktore patria: Integery, Stringy, Floaty, Booleany
# Integery - su to CELE cisla (bez desatinneho miesta)
# Floaty - patria tam aj "NECELE" cisla (s desatinnou ciarkou)
# Stringy - slova alebo vety (teda list charov...)
# Boolean - True | False

# Rozne typy variabilit sa daju rozne spajat

# -> Spajanie dvoch a viacerych stringov stringov
def jeden():
    pozdrav = "Ahoj"
    meno = "Mirek"
    
    spojenie = pozdrav + meno # Spojime "pozdrav" a "meno" do jedneho stringu a ulozime vysledok do variability "spojenie"
    print(spojenie) # Printne sa nam "AhojMirek"
jeden()

# -> Spajanie (scitovanie, odcitovanie, nasobenie, delenie) dvoch a viacerych integerov (pri floatoch postupujeme rovnako)
def dva():
    a = 120
    b = 5
    
    scitanie = a+b # Scitali sme "a" a "b" a vysledok ulozili do variability "scitanie"
    print('Scitanie:',scitanie)

    odcitovanie = a-b # Odcitali sme od "a" hodnotu "b" a vysledok ulozili do variability "odcitovanie"
    print('Odcitanie:',odcitovanie) 

    nasobenie = a*b # Vynasobili sme hodnotu "a" hodnotou "b" a vylseodk ulozili do variability "nasobenie"
    print('Nasobenie:',nasobenie)

    delenie = a/b # Vydelili sme hodnotu "a" hodnotou "b" a vysledok ulozili do variability "delenie"
    print('Delenie',delenie)

dva()

# -> Premienanie typov na ine typy (ak sa da)
def tri():
    a = input('Zadaj nejake cislo:') # Vieme, ze do inputu dokazeme dosadzovat nejake hodnoty, tie su vsak typu string a neda sa s nimi pracovat ako s integermi (porovnavat > < alebo scitovat)
    
    print(type(a)) # Mozeme si to oveirt prikazom "type()", ktory nam returtne o aky typ variability ide
    
    int(a) # Pre zmenu typu danej variability do typu integer pouzijeme prikaz "int()"

    if a > 10: # Vdaka tomuto je tato variabilita typu integer a ide porovnovat, odcitovat, scitovat, nasobit ...................................
        print('Je to vacsie!')

tri() #Takymto sposobom idu premienat nasledujuce typy "int()" - na integer, "str()" - na string, "float()" - na float, "bool()" - na boolean
      #samozrejme nie vzdy ide premenit nejaky typ na iny, napriklad string "pes" nepremenime na integer, ale vyhodi nam to error
      #v takom pripade existuje prikaz "try", ktory ukazem ako funguje niekedy nabuduce
