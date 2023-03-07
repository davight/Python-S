import turtle
import random as r
from misc import n_uholnik

tu = turtle.Turtle()
tu.speed(0)
turtle.delay(0)

def stvorec(velkost: int) -> None:
    for _ in range(5):
        tu.left(90)
        tu.fd(velkost)

def trojuholnik(velkost: int) -> None:
    tu.right(90)
    for _ in range(2):
        tu.left(120)
        tu.forward(velkost)

def prve_cvicenie(pocet_domov):

    # Zadanie:
    # Vykresli vedla seba n domcekov rozne
    # velkych a kazdy vyfarebny inou farbou.

    for i in range(pocet_domov):
        tu.fillcolor(r.choice(["red", "green", "blue"]))
        velkost = r.randint(30, 60)
        if i != 0: tu.fd(velkost)
        stvorec(velkost)
        trojuholnik(velkost)
        tu.left(30)
        tu.fd(velkost)
        tu.left(90)
        tu.forward(velkost)

prve_cvicenie(10)

def druhe_cvicenie():

    # Zadanie:
    #  Vykresli kruznice do kruhu ci jako.

    for _ in range(18):
        n_uholnik(360, 1, tu)
        tu.left(20)

def tretie_cvicenie():

    # Zadanie:
    #  Vykresli kruznice vedla seba s n medzerou.
    for _ in range(10):
        n_uholnik(360, 1, tu)
        tu.fd(10)

tretie_cvicenie()

def stvrte_cvicenie():

    # Zadanie:
    #  Vykresli kruznice do kruhu aj s medzerou.

    for _ in range(18):
        n_uholnik(360, 1, tu)
        tu.left(20)
        tu.fd(10)

stvrte_cvicenie()

def piate_cvicenie():

    # Zadanie:
    #  Inicializuj viacero korytnaciek.
    #  A vykresli s nimi nejake tvary.

    tu_dva, tu_tri, tu_styri, tu_pat = turtle.Turtle(), turtle.Turtle(), turtle.Turtle(), turtle.Turtle()
    for obj in (tu, tu_dva, tu_tri, tu_styri, tu_pat):
        obj.pu()
        obj.setpos(r.randint(-100, 100), r.randint(-100, 100))
        obj.pd()
        n_uholnik(360, 1, obj)

piate_cvicenie()

turtle.mainloop()
