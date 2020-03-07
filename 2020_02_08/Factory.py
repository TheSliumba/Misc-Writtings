"""
Ceche dirba darbuotojai, kurie gamina automobilių detales.
Darbuotojai identifikuojami pagal ID [0-9].
Detalės identifikuojamos raidėmis [A-H].

Direktorius nusprendė, kad nori sekti darbuotojų našumą.
Bei perskirstyti detalių gamybą darbuotojams, kurie šias
detales pagamina greičiausiai.

Detalių gamybos preliminarūs laikai būna:
A: 100 - 300 min
B: 150 - 400 min
C: 180 - 360 min
D: 250 - 450 min
E: 200 - 320 min
F: 800 - 1400 min
G: 600 - 900 min
H: 440 - 880 min

Užduotis:
1) Sugeneruoti failą su bandomaisiais duomenimis.
   Kiekvienas darbuotojas turi būti bent kartą pagaminęs
   po kiekvienos rūšies detalę. Eksportuojama į CSV failą
   kur stulpeliai yra: darbuotojo_id, detalės_id, laikas
   (Naudoti random.randint(nuo, iki) generuoti laikui,
   kiek truko pagaminti detalę)
"""
import random
import csv

def generuoti_duomenis():
    def atsitiktiniai_duom(nuo_iki_laikai):
        nuo,iki = nuo_iki_laikai
        return random.randint(nuo,iki)

    gamybos_laikai={
        "A":(100, 300),
        "B":(150, 400),
        "C":(180, 360),
        "D":(250, 450),
        "E":(200, 320),
        "F":(800, 1400),
        "G":(600, 900),
        "H":(440, 880),
    }

    return [[darbuotojo_id, dalies_id, atsitiktiniai_duom(gamybos_laikai[dalies_id])]
            for darbuotojo_id in range(10) for dalies_id in "ABCDEFGH"]

def eksportuoti_duomenu_faila():
    with open("duomenys.csv", 'w',encoding="utf-8",newline="") as f:
        writer = csv.writer(f)
        writer.writerow(['darbuotojo_id', 'detales_id', 'laikas'])
        writer.writerows(generuoti_duomenis())

def read_csv(file):
    with open(file) as f:
        return list(csv.DictReader(f))

duomenys = read_csv("duomenys.csv")
detales = "ABCDEFGH"

for i in detales:
    detales_gamybos_duom = [d for d in duomenys if d['detales_id']==i]
    darbuotojas = min(detales_gamybos_duom, key=lambda x:x['laikas'])
    print(f'detalę {i} per {darbuotojas["laikas"]} min, pagamina darbuotojas kurio id yra {darbuotojas["darbuotojo_id"]}')

detaliu_gamyba = {d:{} for d in detales}
for d in duomenys:
    detale = d["detales_id"]
    d_id = d["darbuotojo_id"]
    laikas = int(d["laikas"])
    detaliu_gamyba[detale][d_id] = laikas

from itertools import permutations
variantai = list(permutations(list(range(10)),8))

def apsjkaiciuoti_laika(variantas):
    visas_laikas = 0
    for det, darb in enumerate(variantas):
        visas_laikas += detaliu_gamyba[det][darb]
        return visas_laikas

optimalus = min(variantai, key=apsjkaiciuoti_laika)
print(optimalus)
if __name__ == '__main__':
    pass