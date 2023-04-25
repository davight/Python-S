import turtle
import math

korytnacka = turtle.Turtle()
korytnacka.speed(1)

def prve_cvicenie(num: int, size=120):
    # Zadanie:
    #  Vykresli trojuholniky do seba.
    #  Kde zakazdym novy vnoreny je otoceny
    #  a mensi ako ten predchadzajuci.

    for _ in range(3):
        korytnacka.fd(size)
        korytnacka.left(120)
    korytnacka.forward(size/2)
    korytnacka.left(60)
    if num == 1: return
    prve_cvicenie(num-1, int(size/2))

#prve_cvicenie(4)

def druhe_cvicenie(num: int, size=120):
    # Zadanie:
    #  Vykresli stvorce do seba.
    #  Kde zakazdym novy vnoreny je otoceny
    #  a mensi ako ten predchadzajuci.

    for _ in range(4):
        korytnacka.fd(size)
        korytnacka.left(90)
    korytnacka.forward(size/2)
    korytnacka.left(45)
    size = math.sqrt(size**2+size**2)/2
    print(size)
    if num == 1: return
    druhe_cvicenie(num-1, int(size))

druhe_cvicenie(4)
turtle.mainloop()
