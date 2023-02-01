import tkinter as tk
import random as ra

ca = tk.Canvas(height=500, width=1000, background="white")
ca.pack()

# Zadanie:
#  Importni dva lubovolne obrazky a pouzi
#  ich ako objekty, ktore sa budu navzajom
#  pretekat po platne. Prvy objekt, ktory
#  sa dostane na pravu stranu vyhrava.

class Nastavenia:
    zaciatok: int = 100
    ciel: int = 900
    range_rychlosti: tuple = 5, 12
    update_rychlost: int = 100  # v MS

ciel = ca.create_line(Nastavenia.ciel+88, 0, Nastavenia.ciel+88, 500, width=5)

# Prvotne vykreslenie oboch aut na zaciatku.
red_car_img = tk.PhotoImage(file="red_car.png")
ca.create_image(Nastavenia.zaciatok, 150, image=red_car_img, tags="red_car")

blue_car_img = tk.PhotoImage(file="blue_car.png")
ca.create_image(Nastavenia.zaciatok, 300, image=blue_car_img, tags="blue_car")

vyhral = False

while not vyhral:
    for tag in "blue_car red_car".split():
        ca.move(tag, ra.randint(Nastavenia.range_rychlosti[0], Nastavenia.range_rychlosti[1]), 0)
        if ca.coords(tag)[0] >= Nastavenia.ciel:
            ca.create_text(400, 100, font="Arial 25 bold", text=f"Vyhralo {tag.replace('_car', '')} auto")
            vyhral = True; break
    ca.after(Nastavenia.update_rychlost); ca.update()

tk.mainloop()
