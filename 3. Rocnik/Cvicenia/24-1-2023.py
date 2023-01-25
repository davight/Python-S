import tkinter as tk
ca = tk.Canvas(height=500, width=500)
ca.pack()

# Zadanie:
#  Vykresli ciary na zaklade kliknutia
#  sipok na klavesnici.

sur, pohyb = [250, 250, 250, 250], 10
ca.create_line(tuple(sur), width=3, tags="line")

def klik(key):
    global sur, pohyb

    name = key.keysym.lower()
    match name:
        case "up": sur.extend([sur[-2], sur[-1] - pohyb])
        case "down": sur.extend([sur[-2], sur[-1] + pohyb])
        case "right": sur.extend([sur[-2] + pohyb, sur[-1]])
        case "left": sur.extend([sur[-2] - pohyb, sur[-1]])

    ca.coords("line", sur)

ca.bind_all("<Key>", klik)
tk.mainloop()


import tkinter as tk

root = tk.Tk()
root.title("Mittens vracia uder")
canvas = tk.Canvas(root, width=500, height=500, bg="silver")
canvas.pack()

#Zadanie: importni random png subor do platna a nech sa hybe wasd.
obr = tk.PhotoImage(file = "notmiguel.png")
canvas.create_image(250, 250, image = obr, tags = "gato")
move = 20

def kiten(event):
    if event.keysym == "Right":
        canvas.move("gato", move, 0)
    elif event.keysym == "Left":
        canvas.move("gato", -move, 0)
    elif event.keysym == "Up":
        canvas.move("gato", 0, -move)
    elif event.keysym == "Down":
        canvas.move("gato", 0, move)

canvas.bind_all("<Key>", kiten)
canvas.mainloop()
