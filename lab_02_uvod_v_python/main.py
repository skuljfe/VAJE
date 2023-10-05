from cgi import print_form
from operator import truediv


def printanje(niz):
    print(niz)

def sprejemnljivka(vrednost):
    x=vrednost
    print(x)

def vrsta_sprejemljivke(vrednost):
    x=vrednost
    print("vrsta sprejemljivke je: " + str(type(x)))

def vnost():
    starost=input("vnesi koliko si star ")
    print("star si " + starost)

def lists():
    sadnje=["ananas", "jagoda", "jabolko", "cesnja"]
    hrana={
        "sadnje":["jabolko", "pomaranca"],
        "zelenjava": ["solata, krompir"],
        "pijaca": ["pivo", "vino"]
    }
    print(sadnje)
    print(sadnje[0])
    print(hrana['pijaca'][0])

def kontrola(velikost):
    if(velikost>3):
        return True
    else:
        return False

def zanke(stevilo_ponovitev):
    x=0
    for i in range(stevilo_ponovitev):
        x+=1.3
    print(x)

def trikotnik(stevilo_nivojev):
    for i in range(stevilo_nivojev):
        print(" "*(stevilo_nivojev-i), end="")
        print("x"*(i*2+1))

#printanje("test")
#sprejemnljivka(4)
#vrsta_sprejemljivke(True)
#vnost()
#lists()
#print(kontrola(2))
#zanke(5)
trikotnik(7)