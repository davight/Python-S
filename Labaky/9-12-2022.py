# Cvicenia z labakov.
# Den - 9.12.2022 ; Skupina - II

# +++> Info:
#
# - Dictionary v pythone sluzi na ukladanie
#   dat pomocou priradovanie ich k nejakym
#   hodnotam. ( key: value ) Oznacuju sa
#   tymito zatvorkami {} ( Neviem jak sa
#   to nazyva v Slovencine. )
#   @ Priklad:
#       myDict = {
#           "meno": "Filip",
#           "id": 22667121
#       }
#
# - Citanie z dictionary sa robi pomocou
#   volania podla key hodnoty.
#   @ Priklad:
#       print( myDict["meno"] )
#       ( Pouzijem ako priklad nas uz zadefinovany dictionary "myDict" a vytiahnem z neho hodnotu priradenu k "meno" )
#
# - Do dictionary sa vkladaju data pomocou
#   volania key a priradeniu hodnoty ku
#   nemu. Pokial uz key existuje, hodnota
#   bude nahradena novou zadanou hodnotou.
#   @ Priklad:
#       myDict["farba"] = "modra"

# ++ Zadanie k prvemu cviceniu:
#   Napis program, ktory vypise dictionary n cisel
#   cisel kde key je o 1 vacsie ako predchadzajuci
#   a value vacsie o 1 ako key, pricom key zacina
#   na 1. ( Priklad: {1:2, 2:3, 3:4... n} )
# ++ Obmedzenia:
#   n nacitaj z inputu

# Mozne riesenie:
def prveCvicenie():
    count = int(input("Zadaj po ake cislo sa ma dictionary vygenerovat: "))

    cisla = {i: i + 1 for i in range(1, count)}
    return print(cisla)

prveCvicenie()

# ++ Zadanie k druhemu cviceniu:
#  Napis program, ktory vypise dictionary
#  pismen a pocet ich vyskytov v nejakom
#  texte. ( Priklad: text = "Hello World"
#  output = {H: 1, e: 1, l: 3, o: 2...} )

# Mozne riesenie:
def druheCvicenie():
    text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the..."

    vyskyt = {i: text.count(i) for i in set(text) }
    return print(vyskyt)

druheCvicenie()
