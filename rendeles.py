import szamla

leves= ["Gulyás leves","Tojás leves"]
leves_ar= [1800,1400]
foetel= ["Lasagne", "Rizottó"]
foetel_ar= [2000,1800]


def rendeles(etel, etel_ar):
    valasztott_etelek: list = [] #append
    kerdes1: str = input("Kér levest (I/N)?")
    while not (kerdes1 == "I" or kerdes1 == "N"):
        print("Hiba! Csak I / N válasz adható meg")
        str = input("Kér levest (I/N)?")
    if kerdes1 == "I":
        kerdes2: str = input("Melyik levest kéri (1/2)?")
        if kerdes2 == "1":
            valasztott_etelek.append(leves[0])
        elif kerdes2 == "2":
            valasztott_etelek.append(leves[1])
    elif kerdes1 == "N":
        kerdes3: str = input("Kér főételt I/N?")
        while not (kerdes3 == "I" or kerdes3 == "N"):
            print("Hiba! Csak I / N válasz adható meg")
            kerdes3: str = input("Kér főételt I/N?")
        if kerdes3 == "I":
            kerdes4: str = input("Melyik levest kéri?")
            if kerdes4 == "1":
                valasztott_etelek.append(foetel[0])
            elif kerdes4 == "2":
                valasztott_etelek.append(foetel[1])

    return valasztott_etelek



            



    return valasztott_etelek

"""
    kerdes2: str = input("Kér főételt I/N?")
    if kerdes2 == "I" or "i" or "igen" or "Igen":
        valasz2: str = input("Melyik főételt kéri (1/2)?")
        if valasz2 == "1":
            valasztott_foetel= f1
            v_f_ar = f1_ar
        elif valasz2 == "2":
            valasztott_foetel= f2
            v_f_ar = f2_ar



"""







