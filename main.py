import etlap

leves= ["Gulyás leves","Tojás leves"]
leves_ar= [1800,1400]
foetel= ["Lasagne", "Rizottó"]
foetel_ar= [2000,1800]


etlap_meret = 60

etlap.cim("ÉTLAP", etlap_meret)

etlap.szoveg_kiiras("*", "Levesek", "*", etlap_meret)

def lista_kiir(lista,lista_ar):
    i: int = 0
    while i < len(lista):
        etlap.megnevezes_osszeg("*", lista[i],str(lista_ar[i]) + "Ft", "*", etlap_meret)
        i += 1

lista_kiir(leves, leves_ar)

"""etlap.megnevezes_osszeg("*", "1. Gulyás leves", "1800 Ft", "*", etlap_meret)
etlap.megnevezes_osszeg("*", "2. Tojás leves", "1400 Ft", "*", etlap_meret)
"""
etlap.szoveg_kiiras("*", "Főételek", "*", etlap_meret)
lista_kiir(foetel,foetel_ar)
"""etlap.megnevezes_osszeg("*", "1. Lasagne", "2000 Ft", "*", etlap_meret)
etlap.megnevezes_osszeg("*", "2. Rizottó", "1800 Ft", "*", etlap_meret)"""

etlap.cim("JÓ ÉTVÁGYAT!", etlap_meret)

import rendeles

"""rendeles.rendeles("1. Gulyás leves", "1800 Ft", "2. Tojás leves", "1400 Ft", "1. Lasagne", "2000 Ft","2. Rizottó", "1800 Ft")"""
valasztott_etelek = rendeles.rendeles(leves, leves_ar)
print(f"Az általad választott étel: {valasztott_etelek}")


