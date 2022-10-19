# Cvicenie poskytnute Alexom, yay
import random
import tkinter

canvas=tkinter.Canvas()
canvas.pack()


def prva_uloha():
    
    # Zadanie: Vytvorte program, ktory importne z txt suboru farby
    # a vyfarbi na zaklade toho 10 stvorcekov. Kazda farba je
    # oddelena medzerou.
    
    # Variability pre ulozenie pozicie
    # zakladneho (prveho) stvorca 
    x = 30
    y = 30
    
    # Otvorenie suboru a jeho citanie
    subor = open("farbicky.txt", "r")
    exercise = subor.readline()
    
    color = exercise.split()
    
    # Nacitanie stvorcekov
    for farbicka in range(10):
        canvas.create_rectangle(x, y, x + 30, y + 30, fill = color[farbicka])
        x += 30

#prva_uloha()


def druha_uloha():
    
    # Zadanie: Vytvorte program, ktory vykresli 10 kruhov
    # podla zadanych udajov v textovom subore.
    # Udaje: [pozicia_x] [pozicia_y] [polomer] [farba]
    
    # Otvorenie suboru a nacitanie jeho udajov
    subor = open("kruh.txt", "r")
    riadok = subor.readline()
    
    while riadok != "":
        kruh = riadok.split()
        canvas.create_oval(kruh[0], kruh[1], int(kruh[0]) + int(kruh[2]), int(kruh[1]) + int(kruh[2]), fill = kruh[3])    
        # Nacitanie dalsieho riadka
        riadok = subor.readline()
        
#druha_uloha()
