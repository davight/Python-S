import tkinter

tk = tkinter.Canvas(width=800, height=500, bg="white")
tk.pack()

sur = tuple()

def prveCvicenie(mouse):

    # Zadanie:
    # Kazdym klikom sa na danej pozicii
    # vykresli bodka a ta sa spoji s
    # predchadzajucou, ak nejaka je.

    global sur
    print(sur)
    x, y = mouse.x, mouse.y

    if len(sur) != 0:
        tk.create_line(sur, x, y)
    
    tk.create_oval(x - 5, y - 5, x + 5, y + 5, fill="black")
    sur = x, y
 
tk.bind("<Button-1>", prveCvicenie)
tk.mainloop()
