# Listy, abo zoznamy sa pouzivaju na ukladanie viacerych hodnot do jednej variability
# Listy sa daju rozne upravovat, odoberat z nich, pridavat k nim, menit ich poradie.....
# Hodnoty sa v nich MOZU opakovat, hodnoty mozu byt rozne typy (integer, string, float)
# Listy sa definuju pomocou hranatych zatvoriek

# -> Vytvorenie listu a nasledne volanie nejakej hodnoty
def cvicenie1():
    
    a = ["Luli","Pes","Kocka","Valec","Pomoc"] # Vytvorili sme list, ktory obsahuje 5 stringov: "Luli", "Pes", "Kocka", "Valec", "Pomoc"
    print("Cely list:",a) # Printne sa nam cely list

    # Pokial chceme printnut hodnotu, ktora sa nachadza na urcitom poradi pouzijeme list[cislo]
    # Musime vsak pamatat ze prva hodnota ma index 0
    # Cize v nasom pripade hodnota "Luli" je prva v poradi a ma index 0 ; "Pes" je druha v poradi a ma index 1 ; "Kocka" je tretia v poradi a ma index 2 .....
    # ["a","b","c","d"] <-- Poradie hodnot
    #   0 , 1 , 2 , 3   <-- Ich index
    
    # Ziskanie n hodnoty z listu:
    print("Druha hodnota v liste:",a[1]) # Rozhodli sme sa printnut druhu hodnotu z listu "a", cize s indexom 1. (To nam printne "Pes")

    # Pokial chceme printnut naraz viacero hodnot z listu, pouzijeme moznost zadefinovat rozsah pomocou "od_index:do_index"
    # Ziskanie n hodnot v x rozsahu:
    print("Printneme 1. az 3. hodnotu z listu:",a[0:3]) # 0 je redundantna, cize ak ju vynechame automaticky zacne od zaciatku (Toto nam printne "Luli", "Pes", "Kocka", "Valec")

    # Pokial chceme printnut urcite hodnotu z pravej strany (alebo jednoducho poslednu), pouzijeme zaporne cisla, cize pocitame z pravej strany...
    # Ziskanie poslednej hodnoty z listu:
    print("Posledna honota v liste je:",a[-1])
cvicenie1()


# -> Pridavanie do listu
def cvicenie2():
    import random

    # +--------------
    pes = 132+3
    list = [random.randint(1,5),pes,"Ahoj",245,True] # List s nahodnymi vecami, ktore mi v tento moment napadli...
    
    # Aktualne nas list vyzera takto:
    print("Takto vyzera neupraveny list: ",list)

    # +--------------
    # Pre pridanie hodnoty do listu pouzijeme funkciu append("to co chceme pridat")
    # Pridana hodnota sa da na koniec listu
    list.append("Chris") # Pridali sme do listu string "Chris"

    list.append(5) # Pridali sme to listu integer 5

    list.append(["Jeden","Dva"]) # Pridali sme do listu DALSI list s hodnotami "Jeden" a "Dva"

    # Takto vyzera nas list teraz:
    print("Takto vyzera list po pridani urcitych hodnot pomocou append: ",list)

    # +--------------
    # Do listov sa davaju hodnoty aj "vsuvat", cize ich vlozime na urcity index a nie na posledne miest
    # Robi sa to pomocou funkcie insert("index", "hodnota")
    
    # Priklad:
    list.insert(4,"Jablko") # Vsunuli sme hodnotu "Jablko" na 4 index v liste

    # Takto vyzera nas list teraz:
    print("Takto vyzera list po vsunuti urcitej hodnoty pomocou insert: ",list)
cvicenie2()


# -> Odstranovanie z listu
def cvicenie3():
    import random

    list = [2,"Hruska","Marek","Aplikacny","Dejepis"] # List s vecami, ktore mi aktualne napadli...
    # Aktualne nas list vyzera takto:
    print("Takto vyzera neupraveny list: ",list)

    # +-------------
    # Pre odstranenie urcitej hodnoty z listu pouzijeme funkciu remove("hodnotu ktoru chceme odstranit")
    # Vzhladom na to, ze v listoch mozu byt duplikatne hodnoty tak sa odstrani prva, ktoru to zachyti
    # Priklad: Mame list ["Pes","Macka","Pes"] , pouzijeme list.remove("Pes") a zostane nam tento list ["Macka","Pes"]
    
    list.remove("Aplikacny") # Z listu sme odstranili hodnotu "Aplikacny" (Kto by mal rad aplikacny ????)

    list.remove(2) # Z listu sme odstranili hodnotu integer "2"

    # Takto vyzera nas list teraz:
    print("Takto vyzera list po vymazani urcitych hodnot pomocou remove: ",list)

    # +------------
    # Mozu vsak nastat pripady kedy nevieme aku hodnotu chceme odstranit ale chceme odstranit n hodnotu na nejakom indexe (v nejakom poradi)
    # Vtedy sa nam hodi funkcia pop("index"), ktora odstrani hodnotu na danom indexe

    list.pop(2) # V tomto pripade sme odstranili n hodnotu s indexom 2 (3. v poradi..)

    list.pop(random.randint(1,3)) # V tomto pripade sme odstranili n hodnotu s nahodne vybranym indexom od 1 po 3

    # Takto vyzera nas list teraz:
    print("Takto vyzera list po odstraneni urcitej hodnoty pomocou pop: ",list)
cvicenie3()


# -> Hladanie hodnot v liste
def cvicenie4():

    list = ["Nechce","sa","mi","uz","vymyslat","hodnoty","ahoj","ahoj",10] # List s vecami, ktore mi *nenapadli*....
    # Aktualne nas list vyzera takto:
    print("Takto vyzera neupraveny list: ",list)

    # +------------- 
    # Pokial chceme zistit index nejakej hodnoty, ktoru hladame, mozeme pouzit funkciu index("hodnota")
    # Priklad:
    print("Hodnota 'sa' sa nachadza na indexe:", list.index("sa") ) # Nam printne index, na ktorom sa nachadza hodnota "sa" (cize 1)

    # +------------
    # Pokial chceme spocitat urcite hodnoty v liste (kedze sa mozu opakovat) mozeme pouzit funkciu count("hodnota")
    # Priklad:
    print("Hodnota 'ahoj' sa v liste  nachadza:", list.count("ahoj"),"krat" ) # Nam printne cislo 2, pretoze sa hodnota "ahoj" v liste "list" nachadza 2krat...

cvicenie4()

# S listami sa daju robit zaujimave veci, nemam cas vypisat vsetky a zaroven nechcem predbiehat ucivo, toto je taka zakladna
# praca s listami.
