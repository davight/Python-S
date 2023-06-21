import tkinter
import random

canvas = tkinter.Canvas(width=500, height=500)
canvas.pack()

def random_list(hl_velkost: int, sub_velkost: int, typ: str) -> list:
    new_list = []
    for _ in range(hl_velkost):
        match typ:
            case "farba":
                new_list.append(
                    [random.choice(["red", "blue", "yellow", "green"]) for _ in range(sub_velkost)]
                    )
            case "cislo":
                new_list.append(
                    [random.int(1, 5) for _ in range(sub_velkost)]
                )
    return new_list

def prve_cvicenie():
    # Zadanie:
    #  Vykresli 3x3 stvorce na zaklade
    #  farieb v liste
    
    x, y = 0, 0
    farby = random_list(3, 3, "farba")
    
    for farba_list in farby:
        for farba in farba_list:
            canvas.create_rectangle(x, y, x+50, y+50, fill=farba)
            x += 50
        x = 0
        y += 50

prve_cvicenie()

def druhe_cvicenie():
    # Zadanie:
    #  Vykresli sachovnicu

    x, y, value = 0, 0, 0
    for _ in range(64):
        color = "white" if value % 2 == 0 else "black"
        canvas.create_rectangle(x, y, x+20, y+20, fill=color)
        if x == 140:
            x = 0
            y += 20
            value += 2
        else:
            x += 20
            value += 1

druhe_cvicenie()

tkinter.mainloop()
