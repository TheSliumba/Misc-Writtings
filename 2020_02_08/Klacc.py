'''
Sukurima sklypą pateikiant jam kraštines
'''

class Sklypas:
    def __init__(self, plotis, ilgis):
        self.plotis = plotis
        self.ilgis = ilgis

    def perimeters(self):
        self.perimetras = (self.ilgis+self.plotis) *2
        return self.perimetras

    def plotas(self):
        self.plotas = self.ilgis * self.plotis
        return self.plotas

if __name__ == '__main__':
    duomenys = Sklypas(14, 23)
    print(f'Perimetras: {duomenys.perimeters()}, Plotas:{duomenys.plotas()}')