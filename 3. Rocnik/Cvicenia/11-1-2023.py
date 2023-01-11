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

suradnice = 100, 100, 200, 150
ca.create_line(suradnice, tags="line")

def druhe_cvicenie(x: int, y: int) -> None:
    global suradnice
    suradnice = list(suradnice)
    suradnice.extend([x, y])
    ca.coords('line', tuple(suradnice))

def tretie_cvicenie(x: int, y: int) -> None:
    ca.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")

cords = []
def stvrte_cvicenie_klik(x, y):
    global line, cords
    cords = [x, y]
    line = ca.create_line(0, 0, 0, 0, width=4)

def stvrte_cvicenie_motion(x, y):
    cords.extend([x, y])
    ca.coords(line, cords)

def click(mouse):
    #prve_cvicenie(mouse.x, mouse.y)
    #druhe_cvicenie(mouse.x, mouse.y)
    stvrte_cvicenie_klik(mouse.x, mouse.y)
    pass

def move(mouse):
    #tretie_cvicenie(mouse.x, mouse.y)
    stvrte_cvicenie_motion(mouse.x, mouse.y)

ca.bind("<Button-1>", click)
ca.bind("<B1-Motion>", move)
tkinter.mainloop()


