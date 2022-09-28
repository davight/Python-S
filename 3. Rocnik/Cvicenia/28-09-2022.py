def prve_cvicenie():
    
    # Zadanie: Medzi kazde pismeno sa vlozi velke X
    # Priklad: kvet -> kXvXeXt
    slovo = input("Zadaj lubovolne slovo: ")
    
    # Slovo premenime na list a do kazdej "medzery" vlozime "X"
    slovo_list = "X".join(list(slovo))

    # Printneme
    print(slovo_list)

prve_cvicenie()
