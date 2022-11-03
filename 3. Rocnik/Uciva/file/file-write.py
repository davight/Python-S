# ++> Funkcie write() a writelines()
#  Ako hovori samotny nazov, funkcia write a
#  writelines sluzi na vkladanie textu do suboru.
#  Tip:
#   Pri vkladani do suboru nezabudni pouzit "w"
#   mod pri otvarani suboru !

#  ++ Funkcia write()
#   vlozi prave jeden string do suboru

#  ++ Funkcia writelines()
#   vlozi vsetky itemy z listu do suboru

# Path k suboru do, ktoreho ideme pisat
path = r'C:\Users\PC\Desktop\cicky.txt'


# Priklad pouzitia funkcie write()
def prikladJeden():

    # Otvorime subor s modom 'w'
    subor = open(path, 'w')

    # Ideme do neho zapisat nejake hovadiny
    subor.write("Mam rad palacinky.")
    subor.write("Aj s cokoladou ale hlavne s jahodovym dzemom.")

    # Po otvoreni suboru si mozeme vsimnut, ze vety
    # boli napisane vedla seba a neboli oddelene
    # novym riadkom. Pre pripad, ze chceme vety oddelit
    # novym riadkom mozeme pouzit newline character "\n".
    # Priklad vyuzitia:
    subor.write("\nTato veta je v novom riadku!")
    subor.write("\nDokonca aj tato! ! !")

    subor.close()

prikladJeden()

# Priklad pouzitia funkcie writelines()
def prikladDva():

    # Otvorime subor s modom 'w'
    subor = open(path, 'w')

    # Vytvorime si list, ktory ideme vlozimt do suboru
    zoznamZiakov = ["Marko", "David", "Alex", "Mario", "GigaNigga"]

    # Vlozime do suboru cely list
    subor.writelines(zoznamZiakov)

    # Po otvoreni suboru si mozeme vsimnut, ze zoznam mien
    # je znova v jednom riadku. Pokial ich chceme oddelit
    # novym riadkom, tak mozme priamo upravit list a za
    # kazdym itemom dopisat newline character "\n".
    # ["Marko\n", "David\n", "Alex\n", "Mario\n", "GigaNigga\n"]

    # Alebo loopnut cez list a pridavat itemy s newline characterom.
    [ subor.write(item+"\n") for item in zoznamZiakov ]

prikladDva()












