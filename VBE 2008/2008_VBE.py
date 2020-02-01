class Bus:
    def __init__(self, marsrutas, keleiviai):
        self.marsrutas = []
        self.keleiviai = []
        self.stat = {}
        self.islipe = {}
        self.ilipe = {}

    def pridet(self, marsrutas, keleiviai):
        self.marsrutas.append(marsrutas)
        self.keleiviai.append(keleiviai)

    def skaiciuoti(self):
        k = 0
        for i in self.marsrutas:
            if int(i) in self.stat:
                self.stat[int(i)] += int(self.keleiviai[k])
            else:
                self.stat[int(i)] = int(self.keleiviai[k])
            k+=1

    def islipo(self):
        k = 0
        for i in self.marsrutas:
            if int(i) in self.islipe:
                if int(self.keleiviai[k]) < 0:
                    self.islipe[int(i)] += int(self.keleiviai[k])
            elif int(self.keleiviai[k]) < 0:
                    self.islipe[int(i)] = int(self.keleiviai[k])
            else:
                self.islipe[int(i)] = 0
            k += 1

    def ilipo(self):
        k=0
        for i in self.marsrutas:
            if int(i) in self.ilipe:
                if int(self.keleiviai[k]) > 0:
                    self.ilipe[int(i)] += int(self.keleiviai[k])
            elif int(self.keleiviai[k]) > 0:
                self.ilipe[int(i)] = int(self.keleiviai[k])
            else:
                self.ilipe[int(i)] = 0
            k += 1

    def israryt(self):
        for k,v in sorted(self.stat.items(),key=lambda x:[x]):
            print(f'Marsrutas: {k}, Išlipo: {self.islipe[k]}, Įlipo: {self.ilipe[k]}, Netto rezultatas: {v}')


with open("U1.txt") as f:
    duomenys = list(f)
duom = [duomenys[i].strip() for i in range(len(duomenys)) ]
duom = duom[1:]
busai = Bus("Marsrutas", "Keleiviai")

for i in duom:
    busai.pridet(i.split()[0], i.split()[1])

print(f'Maršrutai pagal stebėjimą: {busai.marsrutas}')
print(f'Keleiviai pagal stebėjimą: {busai.keleiviai}')
busai.skaiciuoti()
busai.islipo()
busai.ilipo()
print(f'Suskaičiuoti bendro keleiviai: {busai.stat}')
print(f'Suskaičiuoti išlipę keleiviai: {busai.islipe}')
print(f'Suskaičiuoti įlipę keleiviai: {busai.ilipe}')
busai.israryt()
