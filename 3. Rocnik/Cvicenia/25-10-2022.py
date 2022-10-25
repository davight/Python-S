import tkinter

canvas=tkinter.Canvas()
canvas.pack()

def prve_cvicenie():
    
    # Zadanie:
    # V subore je 12 riadkov, ktore predstavuju farby
    # uloohu je vykreslit 12 stvorcekov, ktore budu mat
    # dane farby.
    
    # Otvorime subor a precitame z neho vsetky riadky,
    # ktore nasledne vlozime do listu
    subor = open("farby.txt.txt")    
    list = subor.read().split("\n")
    
    # Suradnice prveho stvorca
    x = y = 20
    
    # Vykreslime tolko stvorcekov, kolko bude treba
    for farba in list:
        
        # Ak sme uz pridaleko tak dame dalsi riadok
        if x >= 200:
            x = 20
            y += 20
        
        # KRESLENIE
        canvas.create_rectangle(x-10, y-10, x+10, y+10,fill=farba)
        x += 20

    tkinter.mainloop()    

#prve_cvicenie()

def druhe_cvicenie():
    
    # Moj vymysel
    # Stvorceky ktore su zadane podla suboru
    # Nacitanie suboru a splitnutie
    subor = open("platno.txt")
    riadky = subor.read().split("\n")
    
    x = y = 20
    
    for riadok in riadky:
        
        # Riadok obsahuje x pocet farieb
        farby = riadok.split()
        
        for farba in farby:
            
            # KRESLENIE
            try:
                canvas.create_rectangle(x-10,y-10,x+10,y+10,fill=farba)
            except:
                penis = 10
            
            x += 20
        
        y += 20
        x = 20

    tkinter.mainloop()
#druhe_cvicenie()

def tretie_cvicenie():
    
    # Zadanie
    # Vypiste vsetky farby zo suboru v jednej premennej
    
    # Otvorime subor a precitame z neho vsetky riadky,
    # ktore nasledne vypiseme vedla seba 
    subor = open("farby.txt.txt")  
    
    # List vsetkych riadkov, z ktorych sme odstranili newline  
    list = subor.read().split("\n")
    
    # String vsetkych hodnot vedla seba
    str = " ".join(list)
    
    print(f'Farby: {str}')
    
#tretie_cvicenie()
