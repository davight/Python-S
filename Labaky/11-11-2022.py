# Cvicenia z labakov.
# Den - 11.11.2022 ; Skupina - II

# +++> Info:
#
# - V pythone definovanie viacerych variabilit SUCASNE je
#   totalne jednoduche. Pre oddelenie staci na oboch stranach
#   pouzit ',' separator.
#   @ Priklad:
#       a, b = 22667121, "Foo";
#   ( Do variability 'a' sme vlozili integer 22667121 a do 'b' String "Foo". )
#
# - Pokial chceme do variability zadefinovat xy argumentov
#   mozeme pouzit "*arg" parameter. Data budu vo variabilite
#   v liste.
#   @ Priklad:
#       a, *b = 2423, 4232, "Foo", "Bar", 43923
#       ( Do variability 'a' sa vlozi iba int 2423, ostatne data si pozbiera variabilita 'b' )

# ++ Zadanie k prvemu cviceniu:
#   Napis program, ktory prehodi hodnoty
#   dvoch variabilit.
# ++ Obmedzenia:
#   Keep it simple, Jakub, Jakub!

# Mozne riesenie:
def prveCvicenie():

    a = 4239
    b = 12
    a, b = b, a

    return print(f"Prehodene hodnoty: \n a = {a} \n b = {b}")

prveCvicenie()

# ++ Zadanie k druehmu cviceniu:
#    Napis parser s prikazmi: print / plus / minus
#    + print: vypise kazdy argument za prikazom.
#    + plus: scita vsetkych n argumentov.
#    + minus: odcita vsetky argumenty od prveho

# Mozne riesenie:
def druheCvicenie():

    while True:

        cmdArgs = input("> ").split()
        while len(cmdArgs) < 1:
            cmdArgs = input("> ").split()

        mainArg, args = cmdArgs[0], cmdArgs[1:]
        match mainArg:

            case "print":
                if len(args) != 0:
                    print( " ".join(args) )
                else:
                    print("++ Few arguments provided.")

            case "plus" | "+":
                # Filip, nie, NECHCE sa mi robit to cez if elif
                try:
                    numbers = [ int(i) for i in args ]
                    print( sum(numbers) )
                except ValueError as error:
                    print(f"++ Expected integers. \n Error: {error}")
                except IndexError as error:
                    print(f"++ Few arguments provided. \n Error: {error}")

            case "minus" | "-":
                # Filip, nie, NECHCE sa mi robit to cez if elif
                try:
                    numbers = [ int(i) for i in args ]
                    print( numbers[0] - sum(numbers[1:]) )
                except ValueError as error:
                    print(f"++ Expected integers. \n Error: {error}")
                except IndexError as error:
                    print(f"++ Few arguments provided. \n Error: {error}")

            case "nasobenie" | "*":
                try:
                    numbers = [ int(i) for i in args ]
                    cinitel = numbers[0]
                    for nasobok in numbers[1:]:
                        cinitel *= nasobok
                    print( cinitel )
                except ValueError as error:
                    print(f"++ Expected integers. \n Error: {error}")
                except IndexError as error:
                    print(f"++ Few arguments provided. \n Error: {error}")

            case "delenie" | "/":
                try:
                    numbers = [ int(i) for i in args ]
                    delenec = numbers[0]
                    for delitel in numbers[1:]:
                        delenec /= delitel
                    print( round(delenec, 2) )
                except ValueError as error:
                    print(f"++ Expected integers. \n Error: {error}")
                except IndexError as error:
                    print(f"++ Few arguments provided. \n Error: {error}")
                except ZeroDivisionError as error:
                    print(f"++ Division by zero is not possible. \n Error: {error}")

            case "faktorial" | "!":
                if len(args) != 1:
                    print(f"Invalid number of arguments provided.\n Required: 1")
                else:
                    try:
                        cislo = odpoved = int(args[0])
                        for i in range(1, cislo-1):
                            odpoved *= cislo - i
                        print(odpoved)
                    except ValueError as error:
                        print(f"++ Expected integer. \n Error: {error}")

            case "stop":
                return

            case "help" | 'h' | "?":
                print("++ Currently available commands: \n"
                      "print [value(s)] \n"
                      "plus [int], ..., \n"
                      "minus [int], ..., \n"
                      "nasobenie [int], ..., \n"
                      "delenie [int], ... \n"
                      "factorial [int]\n"
                      "stop\n"
                      "help")

            case _:
                print( f"++ Invalid command. \n Command: {mainArg}" )

druheCvicenie()
