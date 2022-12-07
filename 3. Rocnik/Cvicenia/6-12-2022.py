import tkinter

tk = tkinter.Canvas(width=500, height=500, bg = "white")
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


def tretieCvicenie():

    import sys

    velkost = int(input("Zadaj velkost stvorcov: "))
    pocet = int(input("Zadaj, kolko stvorcov chces: "))

    startx = starty = 20
    stvorce, count = {}, 0

    for _ in range(1, pocet + 1):
        
        if startx + velkost > 500:
            startx = 20
            starty += velkost

        if starty + velkost > 500:
            print("Max stvorcov {} so velkostou".format(count, velkost))
            sys.exit() 

        suradnice = startx, starty, startx + velkost, starty + velkost
        farba = "white"
        stvorce[suradnice] = farba
        tk.create_rectangle(suradnice)
        
        count += 1
        startx += velkost
        

    def main(mouse):

        x, y = mouse.x, mouse.y

        for stvorec in stvorce:
            
            farba = stvorce[stvorec]
            startx, starty, endx, endy = stvorec[0], stvorec[1], stvorec[2], stvorec[3]

            if startx <= x <= endx and starty <= y <= endy:
                
                newFarba = farby(farba)
                tk.create_rectangle(startx, starty, endx, endy, fill=newFarba)
                stvorce[stvorec] = newFarba

    tk.bind("<Button-1>", main)

    def farby(akt):
        
        colors = ["red", "blue", "green", "white"]
        if akt not in colors:
            return "white"

        poz = colors.index(akt) + 1
        if poz > len(colors) - 1:
            return colors[0]
        
        return colors[poz]


tretieCvicenie()

#tk.bind("<Button-1>", prveCvicenie)
#tk.bind("<Button-1>", druheCvicenie)

tk.mainloop()
