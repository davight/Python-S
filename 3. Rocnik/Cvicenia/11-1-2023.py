import tkinter
ca = tkinter.Canvas(height=500, width=500)
ca.pack()

class Velkosti:
    x = 40
    y = 40

suradnice = 250, 250
ca.create_rectangle(suradnice, 250 + Velkosti.x, 250 + Velkosti.y, fill="white", tags="cerveny_stvorec")

def prve_cvicenie(x: int, y: int) -> None:
    
    # Zadanie:
    #  1. Po kliknuti myskou sa lava hrana
    #  stvorca posunie na suradnice mysky.
    #  2. Na zaklade polohy stvorca sa bude
    #  menit jeho farba.
    
    global suradnice
    
    new_suradnice = x - suradnice[0], y - suradnice[1]
    ca.move("cerveny_stvorec", new_suradnice[0], new_suradnice[1])
    suradnice = x, y
    print(x,y)
    
    x, y = x + Velkosti.x / 2, y + Velkosti.y / 2
    if x == 250 and y == 250:
        # Stred
        ca.itemconfig("cerveny_stvorec", fill="red")
    elif x < 250 and y < 250:
        # Lavy horny roh
        ca.itemconfig("cerveny_stvorec", fill="yellow")
    elif x < 250 and y > 250:
        # Lavy dolny roh
        ca.itemconfig("cerveny_stvorec", fill="green")
    elif x > 250 and y < 250:
        # Pravy horny roh
        ca.itemconfig("cerveny_stvorec", fill="blue")
    else:
        # Pravy dolny roh
        ca.itemconfig("cerveny_stvorec", fill="pink")
    

def click(mouse):
    prve_cvicenie(mouse.x, mouse.y)

ca.bind("<Button-1>", click)
tkinter.mainloop()
