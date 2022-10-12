# Spravovanie suboro v pythone je nuda
# preto ukazem len zakladne funkcie pri
# spravovani roznych suborov cez py.

# ++> Funkcia open()
#  Ako hovori nazov, sluzi na otvorenie nami vybraneho suboru
#  syntax pre funkciu open je 'open("cesta_ku_suboru", "mod")'
#  pre otvorenie suboru nemusime specifikovat ziadny mod.
#  Po otvoreni subor nevypise, iba sa otvori..
#  Pokial chceme nejak upravovat subor mozeme pouzit jeden z
#  z tychto modov:
#  @ Mody:  
#   "a" - otvori subor na pridavanie textu, ak neexistuje tak aj subor vytvori
#   "r" - je default mod, cize ak neuvedieme ziadny tak sa automaticky uvedie tento
#         otvori subor ( na citanie ) a pokial neexistuje vypise error
#   "w" - otvori subor na pisanie, ak neexistuje vytvori ho
#   "x" - vytvori dany subor, ak sa pokusime vytvori UZ existujuci subor vypise error

def priklad_jeden():

    # Ulozime ci cestu k suborum, upravte si podla vas + ten subor si aj vytvorte
    # pri definovani pathu mozes pouzit funkciu r"str" pre raw citanie stringu
    cesticka = r'C:\Users\PC\Desktop\cicky.txt'

    # Otvorime subor na pridavanie
    pridavanie = open(cesticka, "a")

    # Otvorime subor na citanie
    citanie = open(cesticka)

    # Otvorime subor na pisanie
    pisanie = open(cesticka, "w")

    # Pokusime sa vytvorit subor (vypise error lebo nas subor existuje) 
    vytvori = open(cesticka, "x")

priklad_jeden()


# ++> Funkcia read()
#  Otvorit subor je sice pekne ale ak ho necitame alebo inak neupravujeme
#  tak je to pomerne zbytocne..? (ako aqua??)
#  Na citanie CELEHO suboru teda mozeme pouzit funkciu read().
#  do funkcie read(x) mozeme za x dosadit integer, ktory nam
#  udava kolko charakterov sa bude citat ( od zaciatku suboru )
#  Znamenajuc: print(subor.read(10)) printne prvych 10 charakterov
#  zo suboru, ktory je otvoreny vo variabilite "subor".

def priklad_dva():

    # Zadefinujeme si cestu k suboruu
    cesticka = r'C:\Users\PC\Desktop\cicky.txt'

    # Otvorime subor na citanie
    subor = open(cesticka)

    # Vypiseme prvych 10 charakterov suboru
    print(f'\nPrvych 10 charakterov suboru: \n{subor.read(10)}')
    
    # Ideme vypisat dalsich 10 riadkov
    print(f'\nDalsich 10 charakterov suboru: \n{subor.read(10)}')

    # ++> POZOR !
    # Pokial by sme TERAZ vsak chceli vypisat cely subor alebo
    # nejaku cast tak program si pamata, ze sme uz niekde citali
    # a tam kde sme citali tam teraz stoji. Cize ak by sme
    # dali precitat dvakrat 10 charakterov, tak prvykrat vypise
    # od 1 po 10 a druhykrat od 10 po 20.
    # Ak chceme citat subor znova od zaciatku tak ho mozeme
    # zatvorit (funkciou close()) a znova otvorit.

    # Zatvorime ho a a otvorime znova (aby sme zacali citat od zaciatku)
    subor.close()
    subor = open(cesticka)

    # Vypiseme cely subor (vratane novych riadkov atd):
    print(f'\nCely subor: \n{subor.read()}')

priklad_dva()


# ++> Funkcia readline() a readlines()
#  Ako hovori samotny nazov tato funkcia nam umozni citat
#  naraz cely alebo teda vsetky riadky.

def priklad_tri():

    # Zadefinujeme si cestu k suboruu
    cesticka = r'C:\Users\PC\Desktop\cicky.txt'

    # Otvorime subor na citanie
    subor = open(cesticka)

    # Ideme vypisat vsetky riadky ( riadky sa vypisu ako list ( kazdy riadok predstavuje jeden item v liste ) vratane newline tagu (\n) )
    print(f'\nVsetky riadky: \n{subor.readlines()}')

    # POZOR PLATI TO, CO HORE !
    # Teda tym ze sme teraz precitali cely subor
    # tak je "kurzoz" ulozeny na poslednom riadku
    # na jeho konci. Teda ak by sme teraz chceli
    # vypisat prve tri riadky musime subor zatvorit
    # a znova otvorit. ( Existuju zrejme aj ine moznosti
    # ako citat subor od zaciatku ale neviem ich ..? )

   
    # Ideme vypisat prve tri riadky
    # Nemozeme zabudnut ze pokial citame cele riadky tak
    # citame aj newline tag na ich konci "\n" a tym ze pouzivame
    # print na kazdy riadok tak aj samotny print to vypisuje
    # na novy riadok. Cize yk, 2 riadky miesto 1.
    # Toto sa da samozrejme ofajcit, viacerymi sposobmi
    # ukazem 2 najjednoduchsie..?

    # Zatvorime ho a a otvorime znova (aby sme zacali citat od zaciatku)
    subor.close()
    subor = open(cesticka)

    # Ideme vypisat prve tri riadky, ktore budu obsahovat 
    # 2 nove riadky pri vypisovani ( aby ste videli o com kecam )
    print('\nPrve tri riadky ( so zbytocnymi prazdnymi riadkami ): \n')
    
    # Loopneme tolkokrat, kolko chceme vypisat riadkov
    for pocet in range(3):
        print(subor.readline())

    # Zatvorime ho a a otvorime znova (aby sme zacali citat od zaciatku)
    subor.close()
    subor = open(cesticka)

    # Prvy sposob pre vynechanie novych riadkov
    def prvy_sposob():

        print('\nPrve tri riadky ( 1. Sposob bez tolkych prazdnych riadkov ): \n')

        for pocet in range(3):
            # Prvy sposob sa nachadza priamo v printe, end=""
            # ktory donuti print nevypsiovat na novy riadok
            print(subor.readline(), end="")
    
    prvy_sposob()
    
    # Druhy sposob pre vynechanie novych riadkov
    def druhy_sposob():

        print('\nPrve tri riadky ( 2. Sposob bez tolkych prazdnych riadkov ): \n')

        for pocet in range(3):
            # Druhy sposob je built-in python funkcia replace()
            # ktora v stringu nahradi string inym stringom
            # v nasom pripade nahradime "\n" s ""
            riadok = subor.readline().replace("\n","")
            print(riadok)      
    
    druhy_sposob()          
    
priklad_tri()

# TODO: Zapisovanie do suborov, mazanie suborov..