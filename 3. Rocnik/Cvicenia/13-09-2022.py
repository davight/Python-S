# Zadanie:
# Nacitajte tri cisla, pricom prve je najmensia hodnota
# druhe je najvacsia hodnota a z toho sa vybera tretie cislo
# cisel.

import random

def je_to_cislo(znak):
    try:
        int(znak)
        return False
    except ValueError:
        return True

while True:
    
    vstup_str = input("Zadaj: NAJMENSIE CISLO | NAJVACSIE CISLO | POCET VYBEROV (oddelene medzerami) \n")
    vstup_list = vstup_str.split(" ")
    
    if len(vstup_list) != 3:
        print("Nezadal si tri cisla!")
        break
    
    if je_to_cislo(vstup_list[0]) or je_to_cislo(vstup_list[1]) or je_to_cislo(vstup_list[2]):
        print(f"Nezadal si platne cisla!\n Zadane cisla: {vstup_list}")
        break
    
    prve_cislo,druhe_cislo,tretie_cislo = int(vstup_list[0]), int(vstup_list[1]), int(vstup_list[2])
    
    if prve_cislo >= druhe_cislo or tretie_cislo < 1:
        print("Nejake zadane cislo je neplatne")
        break
    
    list_cisel, priemer = [], 0
    
    for i in range(tretie_cislo):
        
        random_cislo = random.randint(prve_cislo,druhe_cislo)
        list_cisel.append(random_cislo)
        priemer += random_cislo
    
    najvacsia_hodnota = max(list_cisel)
    najmensia_hodnota = min(list_cisel)
    priemerna_hodnota = priemer/tretie_cislo 
    
    print(f"Najvacsie hodnota z random cisel bola: {najvacsia_hodnota}")
    print(f"Najmensia hodnota z random cisel bola: {najmensia_hodnota}")
    print(f"Priemerna hodnota z random cisel bola: {priemerna_hodnota}")
    print(f"\n Random cisla boli tieto: {list_cisel}")
