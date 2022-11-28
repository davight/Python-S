def prveCvicenie():

    # Zadanie:
    #  Vypis vetu po riadkoch tak, ze nepresiahne
    #  n pocet charakterov v danom riadku.
    
    count = int(input("Zadaj pocet charaktreov, po ktorych chces vypisovat: "))
    veta = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting"

    # Loopneme cez kazdy nty charakter
    for item in range(0, len(veta), count):

        # Vypisime od aktualnej poziciu po aktualnu + n
        print( veta[item:item + count] )

#prveCvicenie()

def druheCvicenie():

    # Zadanie:
    #  Vypis vetu po riadkoch tak, ze riadok
    #  nepresiahne n pocet charakterov a
    #  zaroven sa nesplitnu slova.
    
    count = int(input("Zadaj pocet charakterov, po ktorych chces vypisovat: "))
    veta = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting"
    
    riadok = ""

    for slovo in veta.split():
        
        # Check ci samotne slovo nema viac
        # charakterov ako nastaveny limit.
        if len(slovo) > count:
            return print("Veta nemoze obsahovat slova, ktore su dlhsie ako tvoj limit!")
        
        # Check ci by nepresahoval riadok n charakterov
        # ak by sme do neho pridali dalsie slovo
        if len(riadok) + len(slovo) > count:
            print(riadok)
            riadok = ""
        
        else:
            riadok += slovo + " "

druheCvicenie()
