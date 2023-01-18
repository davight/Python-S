# Zadanie:
#  Po kliknuti mysky vykresli ciaru od posledneho kliku
#  pricom pri pohybe myskou sa musi zobrazovat ciara podla
#  polohy mysky.

import tkinter as tk
ca = tk.Canvas()
ca.pack()

suradnice_move = None
line = ca.create_line(0, 0, 0, 0)

def click(m):
    global suradnice_move, line

    suradnice_move = m.x, m.y
    line = ca.create_line(0, 0, 0, 0)
    
def move(m):
    global suradnice_move, line
    
    if suradnice_move is None: return
    
    ca.delete(line)
    ca.update()
    line = ca.create_line(suradnice_move, m.x, m.y)

ca.bind("<Motion>", move)
ca.bind("<Button-1>", click)

ca.mainloop()
