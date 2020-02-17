import json
import random
import string

try:
    with open("db.json") as f:
        db = json.load(f)
except FileNotFoundError:
    db = {"test": {"password": "abc123"}}

class Prisijungimas:

    def __init__(self, vartotojo_vardas, slaptažodis):
        self.vartotojo_vardas = vartotojo_vardas
        self.slaptažodis = slaptažodis

    def prisijungti(self):
        return self._vartotojas_egzistuoja() and self._slaptažodis_teisingas()

    def _vartotojas_egzistuoja(self):
        return self.vartotojo_vardas in db

    def _slaptažodis_teisingas(self):
        if len(db[v]) == 1:
            return self.slaptažodis == db[self.vartotojo_vardas]['password']
        else:
            return self.slaptažodis == db[self.vartotojo_vardas]["password"] or self.slaptažodis == db[self.vartotojo_vardas]['password_b']

class Registracija:
    def __init__(self, vartotojo_vardas, slaptažodis):
        self.vartotojo_vardas = vartotojo_vardas
        self.slaptažodis = slaptažodis

    def registruotis(self):
        if self.vartotojo_vardas not in db:
            db[self.vartotojo_vardas] = {"password":self.slaptažodis}
            return True
        return False

class Atstatymas:
    def __init__(self, vartotojo_vardas):
        self.vartotojo_vardas = vartotojo_vardas

    def _generuoti(self):
        strn = string.ascii_letters
        return ''.join(random.choice(strn) for i in range(5))

    def atstatyti(self):
        if self.vartotojo_vardas in db:
            self.slapčius = self._generuoti()
            db[self.vartotojo_vardas].update({"password_b": self.slapčius})
            return True
        return False

while True:
    pasirinkimas = input("Norite prisijungti, atstatyti slaptiką ar registruotis [P/A/R]?\n")
    if pasirinkimas == "P":
        v = input("vartotojo vardas")
        s = input("Slaptažodis")
        p = Prisijungimas(v, s)
        if p.prisijungti():
            print("Pavyko")
            if len(db[v]) == 2 and s == db[v]['password_b']:
                slp = input("Tučtuojau pasikeiskite savo slaptažodį! Naujas: ")
                db[v]["password"] = slp
                db[v]["password_b"] = 'išmesti šitą šiukšlę'
        else:
            print("Nepavyko, kažkas lievai")

    elif pasirinkimas == "R":
        v = input("Vartotojo Vardas")
        s = input("Slaptažodis")
        r = Registracija(v, s)
        if r.registruotis():
            print("Registracija Pavyko")
        else:
            print("Registracija Nepavyko")

    elif pasirinkimas == "A":
        v = input("Vartotojo vardas")
        a = Atstatymas(v)
        a.atstatyti()
        print(f"jūsų naujas slaptikas yra {db[v]['password_b']}")

    else:
        break

with open("db.json") as f:
    f.write(json.dumps(db, indent=2))
