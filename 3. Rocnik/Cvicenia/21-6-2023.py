import random
import tkinter

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

# Zadanie:
#  Vykresli 10x10 platno, kde sa nachadza
#  cesta z bodov A - B. Vytvor hraca (
#  kocku inej farby), ktorej cielom bude
#  prechadzat po danej ceste. Pohyb je
#  nacitavany z klavesnice.

def random_cesta() -> list:
    match random.randint(1, 3):
        case 1:
            path = [
                [0, 0, 0, 0, 2, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 1, 1, 1, 0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 1, 1, 0, 0],
                [0, 1, 1, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            ]
        case 2:
            path = [
                [0, 0, 0, 0, 0, 0, 0, 0, 2, 0],
                [0, 0, 0, 1, 0, 0, 0, 1, 1, 0],
                [0, 1, 1, 1, 1, 0, 0, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 1, 1, 0, 0],
                [0, 1, 1, 1, 0, 1, 1, 0, 0, 0],
                [0, 1, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 1, 0, 1, 1, 1, 0, 0, 1, 0],
                [0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
                [0, 0, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            ]
        case 3:
            path = [
                [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 1, 1, 1, 1, 0],
                [0, 0, 1, 1, 0, 0, 0, 1, 0, 0],
                [0, 1, 1, 0, 0, 0, 1, 1, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            ]
    return path

cesta = random_cesta()
player = None
enabled = True

def vykreslenie() -> None:
    global cesta, player
    x, y = 0, 0

    for riadok in cesta:
        for stvorec in riadok:
            farba = {0:"black", 1:"white", 2:"orange"}[stvorec]
            canvas.create_rectangle(x, y, x+50, y+50, fill=farba, outline=farba)
            x += 50
        y += 50
        x = 0

    player_pos = [cesta[len(cesta)-1].index(1)*50, (len(cesta)-1)*50]
    player = canvas.create_rectangle(player_pos[0], player_pos[1], player_pos[0]+50, player_pos[1]+50, fill="red")

vykreslenie()

def path_checker(pos, pohyb) -> bool:
    try:
        return cesta[int(pos[1] + pohyb[1]) // 50][int(pos[0] + pohyb[0]) // 50]
    except IndexError:
        return 0

def pohyb_event(key) -> None:
    global cesta, player, enabled

    if not enabled: return
    if key.keysym.lower() not in ["up", "down", "left", "right"]: return

    pohyb = { "up": [0, -50], "down": [0, 50], "left": [-50, 0], "right": [50, 0] }[key.keysym.lower()]
    pos = (canvas.coords(player)[0] + 25, canvas.coords(player)[1] + 25)
    bod: int = path_checker(pos, pohyb)
    
    if bod == 0: return
    canvas.move(player, pohyb[0], pohyb[1])
    if bod == 2:
        enabled = False
        canvas.create_text(250, 250,text="Gratulujem!", fill="Orange", font="Arial 40 bold")
    
canvas.bind_all("<Key>", pohyb_event)
tkinter.mainloop()
