from emlos import Macska, Kutya
from keteltu import Madar, Keteltu
from hullo import Hullo

allatok = []
with open("adatok/allatok.txt", "r", encoding="utf-8") as forrasfajl:
    next(forrasfajl)
    for sor in forrasfajl:
        nev, faj, eletkor, szorzet_szine = sor.strip().split(",")
        if faj == "kutya":
            allatok.append(Kutya(nev, int(eletkor), "udvar", szorzet_szine))
        elif faj == "macska":
            allatok.append(Macska(nev, int(eletkor), "ház", szorzet_szine))
        elif faj == "madar":
            allatok.append(Madar(nev, int(eletkor)))
        elif faj == "keteltu":
            allatok.append(Keteltu(nev, int(eletkor)))
        elif faj == "hullo":
            allatok.append(Hullo(nev, int(eletkor)))

for allat in allatok:
    print(allat)