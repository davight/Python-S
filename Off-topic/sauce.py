# Vygeneruje vami zvoleny pocet sauces

# Library pre generovanie "nahodnych" cisel
import random

# Funkcia pre overenie ci bolo zadane cislo
def je_int(str):

    try:
        int(str)
        return True
    
    except ValueError:
        return False

# Main funkcia
def main():

    inputStr = input('Zadaj pocet sauce, ktorych chces vygenerovat: ')

    # Kukneme ci si naozaj zadal cislo
    if not je_int(inputStr):
        # Nezadal si cislo
        return print(f'Nezadal si platne cislo!\nTvoj vstup: "{inputStr}"')
    
    # Premenime input na integer
    pocetSauces = int(inputStr)
    
    # Kukneme ci si nezadal privelku alebo primalu hodnotu
    if pocetSauces > 100 or pocetSauces < 1:
        # TO JE MOC
        return print(f'Tvoje zadane cislo je privela alebo primalo!\nTvoj vstup: "{pocet}"')
    
    list_stranok = []
    for pocet in range(pocetSauces):


        rand_int = random.randint(100000,999999)
        stranka = f"https://nhentai.net/g/{rand_int}"

        list_stranok.append(f'{pocet+1}. sauce je -> {stranka}')
    
    return print("\n".join(list_stranok))

main()

#TODO: Web validator, ci je dana stranka platna