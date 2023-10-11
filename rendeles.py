def rendeles():
    valasztott_leves=""
    valasztott_foetel=""

    kerdes1: str = input("Kér levest (I/N)?")

    if kerdes1 == "I" or "i" or "igen" or "Igen":
        valasz1: str = input("Melyik levest kéri (1/2)?")
        if valasz1 == "1":
            valasztott_leves = "Gulyás leves"
        else:
            valasztott_leves = "Tojás leves"

    elif kerdes1 == "N" or "n" or "Nem" or "nem":
        kerdes2: str = input("Kér főételt I?")
        if kerdes2 == "I" or "i" or "igen" or "Igen":
            valasz2: str = input("Melyik főételt kéri (1/2)?")
            if valasz2 == "1":
                valasztott_foetel= "Lasagne"
            else:
                valasztott_foetel= "Rizottó"







    kerdes2: str = input("Kér főételt (I/N)?")