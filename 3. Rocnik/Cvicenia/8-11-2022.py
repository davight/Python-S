# Funkcia maxCislo pre returnutie najvacsieho cisla
def maxCislo(cisla):

    # Check ci sa jedna o list
    if type(cisla) != type([]):
        return "Nie je list!"

    # Zakladna hodnota
    count = 0
    for cislo in cisla:

        try:
            if cislo > count:
                count = cislo
        except:
            return f"Hodnota {cislo} nie je cislo!"
    
    return count

def minCislo(cisla):

    # Check ci sa jedna o list
    if type(cisla) != type([]):
        return "Nie je list!"

    # Zakladna hodnota
    count = maxCislo(cisla)
    for cislo in cisla:

        try:
            if cislo < count:
                count = cislo
        except:
            return f"Hodnota {cislo} nie je cislo!"
    
    return count

def priemerCislo(cisla):

    # Check ci sa jedna o list
    if type(cisla) != type([]):
        return "Nie je list!"

    # Zakladne hodnoty
    dlzka = len(cisla)
    count = 0

    for cislo in cisla:

        try:
            count += cislo
        except:
            return f"Hodnota {cislo} nie je cislo!"
    
    return count/dlzka


def prveCvicenie():

    # Zadanie:
    #  Vytvor list, ktory obsahuje teploty 7 dni.
    #  Z teplot vypis priemernu teplotu za tyzden,
    #  najmensiu teplotu za tyzden,
    #  najvacsiu teplotu za tyzden.
    # Obmedzenia:
    #  Funkcie na returnutie max, a min teploty si
    #  musis napisat sam.
    
    # List teplot
    teploty = [1,56,22,53,23,"a",1,5]

    max = maxCislo(teploty)
    min = minCislo(teploty)
    priemer = priemerCislo(teploty)
    
    if type(max) == type(min) == type(priemer) == type(int()):
        
        print(f"Maximalna teplota za tyzden bola {max}")
        print(f"Minimalna teplota za tyzden bola {min}")
        print(f"Priemerna teplota za tyzden bola {priemer}")
        return
    
    print(f"Nejaka hodnota v liste {teploty} nie je cislo!")

prveCvicenie()
