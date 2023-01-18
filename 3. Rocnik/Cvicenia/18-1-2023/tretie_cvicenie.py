# Zadanie:
#  Po kliknuti mysky vykresli stvoruhilnik od posledneho
#  kliku pricom pri pohybe myskou sa musi zobrazovat
#  stvoruholnik podla aktualnej polohy mysky.

import tkinter as tk
ca = tk.Canvas()
ca.pack()

suradnice_move = None
rectangle = ca.create_rectangle(0, 0, 0, 0)

def click(m):
    global suradnice_move, rectangle

    suradnice_move = m.x, m.y
    rectangle = ca.create_rectangle(0, 0, 0, 0)
    
def move(m):
    global suradnice_move, rectangle
    
    if suradnice_move is None: return
    
    ca.delete(rectangle)
    ca.update()
    rectangle = ca.create_rectangle(suradnice_move, m.x, m.y)

ca.bind("<Motion>", move)
ca.bind("<Button-1>", click)

ca.mainloop()
