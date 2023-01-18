# Zadanie:
#  Vykresluj ciary spajanim suradnic medzi
#  klikmi. T.j. zakazdym ked kliknes vykresli
#  ciaru od miesta kde si klikol minule.
#  ( Nevykresluj nic pokial klikas prvykrat )

import tkinter as tk
ca = tk.Canvas()
ca.pack()

suradnice = None

def prve_cvicenie(x: int, y: int) -> None:
    global suradnice

    ca.create_oval(x-5, y-5, x+5, y+5)
    
    if suradnice is not None:
        ca.create_line(suradnice, x, y)
    suradnice = x, y

# @Event Handler
def click(mouse):
    prve_cvicenie(mouse.x, mouse.y)


ca.bind("<Button-1>", click)
tk.mainloop()
