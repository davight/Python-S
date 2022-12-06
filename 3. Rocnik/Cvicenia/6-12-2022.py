import tkinter

tk = tkinter.Canvas(width=500, height=500)
tk.pack()

def prveCvicenie(mouse):

    # Zadanie:
    # Vykresli 5 kruznic tam kde kliknes.

    x, y = mouse.x, mouse.y

    for i in range(10, 60, 10):
        tk.create_oval(x-i, y-i, x+i, y+i )


slovo = list("Handlova")
def druheCvicenie(mouse):

    # Zadanie:
    #  Kazdym klikom sa vypise prve pismenko
    #  z listu, ktore sa nasledne odstrani.

    if len(slovo) == 0:
        return tk.create_text(40, 10, text="Koniec slova!")

    x, y = mouse.x, mouse.y
    tk.create_text(x, y, text=slovo[0])
    slovo.pop(0)

stvorce = 9
velkost = 50

sury = 10
start = 20
l = []

for x in range(start, velkost * stvorce, velkost):
    suradnice = x, sury, x + velkost, sury + velkost
    l.append(suradnice)
    temp = tk.create_rectangle(suradnice)

def tretieCvicenie(mouse):

    # Zadanie:
    #  Do platna nakresli vedla seba 8 stvorcekov
    #  vyfarbi ich pomocou kliku

    x, y = mouse.x, mouse.y

    if y < sury or y > sury + velkost or x < start or x > start + 9 * velkost:
        # Nic netrafil
        return

    for stvorec in l:
        startx, starty, endx, endy = suradnice[0], suradnice[1], suradnice[2], suradnice[3]
        if startx >= x >= endx and starty >= y >= endy:
            print("aaa")


    # Trafil




tk.bind("<Button-1>", tretieCvicenie)
#tk.bind("<Button-1>", prveCvicenie)
#tk.bind("<Button-1>", druheCvicenie)

tk.mainloop()
