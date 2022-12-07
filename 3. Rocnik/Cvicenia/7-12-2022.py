def prveCvicenie():

    # Zadanie:
    #  Usporaduvanie cisel v GUI.
    
    # @@@ Importy
    import tkinter
    import sys

    tk = tkinter.Canvas(width=800, height=500, bg = "white")
    tk.pack()

    # @@@ Udaje
    udaje = []
    global zoradene
    zoradene = False

    global x
    global y
    x = 100
    y = 100
    velkost = 50

    # Zadanie zoznamu
    def main():
        print("++ Zadaj cisla, ktore chces neskor zoradovat, oddelene medzerami! \n"
              "Priklad: 1 2 3")
        vstup = input("Cisla: ")

        global listVstup
        listVstup = vstup.split()
        
        # Musi byt spravny pcoet
        if len(listVstup) < 2 or len(listVstup) > 10:
            # List je dlzkou neplatny!
            print("++ Error: Zadal si privela alebo primalo hodnot! Max 9, min 2\n"
                  "Tvoje hodnoty: {}".format(" ".join(listVstup)))
            sys.exit()
        
        # Musia byt cisla
        for i in listVstup:
            try:
                int(i)
            except ValueError:
                print("++ Nejaka hodnota v liste nie je integer!\n"
                      "Tvoje hodnoty: {}".format(" ".join(listVstup)))
                sys.exit()
        
        # Nesmie sa opakovat
        for i in listVstup:
            if listVstup.count(i) > 1:
                print("++ Cisla sa nesmu opakovat!")
                sys.exit()

        # Pridanie nuly
        if not ('0' in listVstup or 0 in listVstup):
            listVstup.insert(0, '0')

    main()

    global zoznamCisel
    zoznamCisel = [ str(i) for i in listVstup ]

    # Prvotne kreslenie
    for cislo in zoznamCisel:
        
        global zoradene
        if zoradene:
            return
        
        realSize = velkost / 2
        # Vykreslime stvorec a text s udajmi
        
        stvorecSuradnice = (x - realSize, y - realSize, x + realSize, y + realSize)
        tk.create_rectangle(stvorecSuradnice)
        
        vykreslenieCisla = str(cislo) if cislo != '0' else ''
        tk.create_text(x, y, text=vykreslenieCisla)
        
        x += velkost
        temp = [stvorecSuradnice, cislo]
        
        udaje.append(temp)


    def update(zoznam):

        global zoradene
        if zoradene:
            return
        
        x = 100
        y = 100
        
        # Vykreslenie prvotnych stvorcov, ako aj ulozenie udajov o ich poziciach
        for index, cislo in enumerate(zoznam):

            realSize = velkost / 2
            #print(zoznam)
            # Vykreslime stvorec a text s udajmi

            stvorecSuradnice = (x - realSize, y - realSize, x + realSize, y + realSize)
            tk.create_rectangle(stvorecSuradnice)

            
            vykreslenieCisla = str(cislo) if cislo != '0' else ''
            tk.create_text(x, y, text=vykreslenieCisla)

            x += velkost

            temp = [stvorecSuradnice, cislo]
            
            udaje[index] = (temp)
        
        #print(info)

    def click(mouse):

        global zoradene
        if zoradene:
            return

        mx, my = mouse.x, mouse.y

        for info in udaje:
            
            suradnice = info[0]
            startx, starty, endx, endy = suradnice[0], suradnice[1], suradnice[2], suradnice[3]

            if startx <= mx <= endx and starty <= my <= endy:
                
                # Klik bol uspesny
                cislo = info[1]
                
                # Klikol na cislo
                global zoznamCisel
                strZoznam = zoznamCisel
                
                pozNuly = strZoznam.index('0')
                pozMeniaceho = strZoznam.index(cislo)
                
                strZoznam = list(strZoznam)
                strZoznam[pozNuly], strZoznam[pozMeniaceho] = strZoznam[pozMeniaceho], strZoznam[pozNuly]
                
                #print(udaje)
                
                for i in range(len(strZoznam)):
                    info = udaje[i]
                    info[1] = strZoznam[i]
                
                tk.delete("all")
                tk.update()
                update(strZoznam)

                zoznamCisel = strZoznam

                # Nie je nahodou zoradeny?                
                if zoradenieCheck(strZoznam):
                    
                    zoradene = True
                    tk.delete("all")
                    tk.create_text(200, 100, text="HOTOVO UZ JE ZORADENY")
                    tk.after(50)
                    
        
    def zoradenieCheck(zoznam):
        
        newZoznam = zoznam.copy()
        
        if newZoznam[-1] != '0':
            return False
        
        newZoznam.pop(-1)
        cisla = [ int(i) for i in newZoznam ]
        
        if sorted(cisla) == cisla:
            return True
        
        return False

    

    #@@@ Bindovanie + loop
    tk.bind("<Button-1>", click)
    tk.mainloop()

prveCvicenie()

