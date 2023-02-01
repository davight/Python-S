import tkinter as tk
import random as ra

ca = tk.Canvas(width=1000, height=500, background="white")
ca.pack()

# Zadanie:
#  Po kliknuti mysky sa zacnu nahodnou
#  rychlostou oproti sebe pohybovat
#  dve rozne auta az pokial sa nestretnu
#  a teda nenaburaju. Pri naburani
#  sa nad nimi zjavi text "BUM".

crashed, hybe = False, False
red_car_img, blue_car_img, bum_img = None, None, None
red_car, blue_car = None, None

def on_click(_):
    global hybe
    if not hybe:
        ca.create_rectangle(0, 0, 1000, 502, fill="white")
        prve_vykreslenie()
        pohyb() 

def prve_vykreslenie() -> None:
    global crashed, red_car_img, blue_car_img, red_car, blue_car

    red_car_img = tk.PhotoImage(file="red_car.png")
    red_car = ca.create_image(50, 250, image=red_car_img, tags="red_car")

    blue_car_img = tk.PhotoImage(file="blue_car.png")
    blue_car = ca.create_image(960, 250, image=blue_car_img, tags="blue_car")

    crashed = False

def pohyb() -> None:
    global crashed, hybe, red_car, blue_car, bum_img
    hybe = True

    while not crashed:
        red_pohyb, blue_pohyb = ra.randint(2, 10), ra.randint(2, 10)

        ca.after(50); ca.update()
        if not ca.coords(red_car)[0] + 84 + red_pohyb >= ca.coords(blue_car)[0] - blue_pohyb - 84:
            ca.move(red_car, red_pohyb, 0)
            ca.move(blue_car, blue_pohyb*-1, 0)
        else:
            bum_img = tk.PhotoImage(file="bum.png")
            ca.create_image(ca.coords(red_car)[0] + 120, 100, image=bum_img)
            crashed, hybe = True, False

prve_vykreslenie()
ca.bind("<Button-1>", on_click)
tk.mainloop()
