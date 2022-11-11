def stvrteCvicenie(n):

    # Zadanie:
    #  Vytvor subor, ktory obsahuje xy cisel
    #  Precitajte z neho vsetky cisla, a vsetky
    #  cisla delitelne n cislom vloz do noveho 
    #  suboru a ostatne (cisla nedelitelne cislom n)
    #  vloz do ineho suboru
    
    with open("C:\\Users\\ziak\\3C IST\\cisla.txt") as subor:
        listCisel = []
        
        for riadok in subor.readlines():
            
            riadok = riadok.replace('[', '').replace(']','').replace(',',' ')
            listCisel += list( map( int, riadok.split() ) )
        
    listDelitelnych = [ str(i) for i in listCisel if i%n == 0 ]
    listNedelitelnych = [ str(i) for i in listCisel if i%n != 0 ]

    with open("C:\\Users\\ziak\\3C IST\\delitelne.txt", 'w') as subor:
        [ subor.write(i + " ") for i in listDelitelnych ]
    
    with open("C:\\Users\\ziak\\3C IST\\nedelitelne.txt", 'w') as subor:
        [ subor.write(i + " ") for i in listNedelitelnych ]

stvrteCvicenie(5)
