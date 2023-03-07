import turtle
import random

t = turtle.Turtle()

def prve_cvicenie():

    # Zadanie:
    # Vykresli spiralovy stvorec.

    for move in range(10, 200, 10):
        t.fd(move)
        t.left(90)

prve_cvicenie()

def druhe_cvicenie():

    # Zadanie:
    # Vykresli spiralu, ktora ma vybrany
    # na zaciatku nahodny uhol.

    uhol = random.randint(30, 170)
    for move in range(10, 200, 10):
        t.fd(move)
        t.left(uhol)

druhe_cvicenie()

def tretie_cvicenie():

    # Zadanie:
    # Vykresli spiralu, ktora ma vybrany
    # na zaciatnu nahodny uhol a kazdym
    # loopom sa uhol zvacsi prave o 1.

    uhol = random.randint(30, 170)
    for move in range(10, 200, 10):
        t.fd(move)
        t.left(uhol)
        uhol += 1

tretie_cvicenie()

turtle.mainloop()
