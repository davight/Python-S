def cvicenie10():
    a = "Dnes je pekne"
    print(a[0:])
#cvicenie10()

def cvicenie11():
    a = "Dnes je streda"
    print(a[9]+a[11]+a[-1])
#cvicenie11()

def cvicenie12():
    a = 172
    b = 60
    print("Karol meria",a,"a vazi",b)
    print("Karol meria {}".format(a))
#cvicenie12()

def cvicenie13(slovo):
    for i in range(0,int(len(slovo)),3):
        print(i+1,"-",i+3,slovo[i:i+3])
#cvicenie13("Python")

def cvicenie14(slovo):
    for i in range(0,int(len(slovo)-2),1):
        print(i,"-",i+2,slovo[i:i+3])
#cvicenie14("Python")

def cvicenie15(slovo):
    count = len(slovo)
    for cislo in range(len(slovo)):
        count -= 1
        print(" "*count,slovo[-cislo-1:])
cvicenie15("Python")
