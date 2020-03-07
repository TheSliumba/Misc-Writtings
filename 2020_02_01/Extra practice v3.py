'''
1) Sukurti klasę Produktas, kuriame saugoma informacija apie produktą.
2) Sukurti Sandėlis klasę, kurioje saugoma informacija apie turimą inventorių.
Inventorius yra produkto klasės objektų sąrašas.
3) Sukurti Sandėlio klasės metodą, kuriuo apskaičiuojama likučių vertė.
'''
from typing import Dict

class Produktas:
    pavadinimas:str = None
    kaina:float = None

    def __init__(self, pavadinimas, kaina):
        self.pavadinimas = pavadinimas
        self.kaina = kaina

class Sandėlis:
    inventorius:Dict[Produktas, int] = None

    def __init__(self):
        self.inventorius = {}

    @property
    def likučių_vertė(self):
        return sum(produktas.kaina * kiekis for produktas, kiekis in self.inventorius.items())

    def rasti_produktą(self, pavadinimas):
        p = [prod for prod in self.inventorius if prod.pavadinimas == pavadinimas]
        if p:
            return p[0]

    def papildyti_inventorių(self, produktas, kiekis):
        turimas_produktas = self.rasti_produktą(produktas.pavadinimas)
        if turimas_produktas is not None:
            self.inventorius[turimas_produktas] += kiekis
        else:
            self.inventorius[produktas] = kiekis

if __name__ == '__main__':
    p1 = Produktas("Obuoliai", 15.2)
    p2 = Produktas("Apelsinai", 24.8)
    sandelis = Sandėlis()
    sandelis.papildyti_inventorių(p1,45)
    sandelis.papildyti_inventorių(p2,12)
    print(sandelis.likučių_vertė)