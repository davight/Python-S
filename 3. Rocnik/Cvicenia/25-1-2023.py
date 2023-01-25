import tkinter as tk

ca = tk.Canvas(height=500, width=500)
ca.pack()

# Zadanie:
#   Importni random png subor do
#   platna a nech sa hybe s WASD.
obr, move = tk.PhotoImage(file="notmiguel.png"), 10
ca.create_image(250, 250, image=obr, tags="gato")

def kiten(key):
    name = key.keysym.lower()

    match name:
        case "right": ca.move("gato", move, 0)
        case "left": ca.move("gato", -move, 0)
        case "up": ca.move("gato", 0, -move)
        case "down": ca.move("gato", 0, move)

ca.bind_all("<Key>", kiten)
ca.mainloop()
