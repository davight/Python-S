import tkinter as tk
import random

# Funkcia move() je tkinter funkcia pre 'jednoduchy'
# pohyb roznych objektov na platne.

# ++ Parametre:
#  n.move(canvas_objekt, posun_x, posun_y)
# + Pricom canvas_objekt musi byt platny objekt
#   alebo jeho tag.
# + posun_x musi byt integer alebo float hodnota
# + posun_y musi byt integer alebo float hodnota

ca = tk.Canvas(height=500, width=500)
ca.pack()

# Ukazka pouzitia:
#  Ideme posunut cerveny stvorec do pravej strany
#  o 250 pixelov a zeleny stvorec posunieme smerom
#  hore o 200 pixelov.

def prva_ukazka():
    cerveny_stvorec = ca.create_rectangle(100, 100, 150, 150, fill="red")
    ca.create_rectangle(300, 300, 350, 350, fill="blue", tags="modry_stvorec")
    ca.update()

    # Pockame 3 sekundy pre posunom
    ca.after(3000)

    # Posuvame cerveny_stvorec o +250 do x osy.
    ca.move(cerveny_stvorec, 250, 0)
    # Posuvame modry_stvorec o -200 do y osy.
    ca.move("modry_stvorec", 0, -200)
    ca.update()

# prva_ukazka()

# Ukazka pouzitia:
#  Ideme posuvat zeleny stvorec nahodne
#  po obrazovke. Cize nahodne po x osy
#  a zaroven nahodne po y osy

def druha_ukazka():
    ca.create_rectangle(100, 100, 150, 150, fill="green", tags="zeleny_stvorec")

    while True:
        ca.update()
        ca.after(1000)

        # Vyberame nahodne od n zaporneho cisla po n kladne cislo
        # pretoze chceme aby sa nahodne mohli posuvat aj opacnym
        # smerom.
        x, y = random.randint(-45, 45), random.randint(-20, 20)
        ca.move("zeleny_stvorec", x, y)

# druha_ukazka()

tk.mainloop()
