# Zadanie:
#  Po kliknuti a drzanim laveho tlacitka na
#  stvorec ho mozeme tahat kliknutie a tahanie
#  s kliknutim mimo stvorca neurobi nic

import tkinter
ca = tkinter.Canvas(height=500, width=500)
ca.pack()

size = 20
suradnice = 250-size, 250-size, 250+size, 250+size
stvorec = ca.create_rectangle(suradnice, width=3)
tahat = False

def click(mouse) -> None:
    global suradnice, tahat

    if mouse.x >= suradnice[0] and mouse.y >= suradnice[1] and mouse.x <= suradnice[2] and mouse.y <= suradnice[3]:
        tahat = True

def move(mouse) -> None:
    global tahat, size, stvorec, suradnice
    if not tahat: return

    ca.delete(stvorec)
    suradnice = mouse.x-size, mouse.y-size, mouse.x+size, mouse.y+size
    stvorec = ca.create_rectangle(suradnice, width=3)
    ca.update()

def unbind(mouse):
    global tahat
    tahat = False

ca.bind("<Button-1>", click)
ca.bind("<B1-Motion>", move)
ca.bind("<ButtonRelease>", unbind)

ca.mainloop()
