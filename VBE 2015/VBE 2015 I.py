'''

Dvidešimt mokinių išsirikiuoja į eilę taip: kairėje stovi dešimt mergaičių, o dešinėje – dešimt
berniukų. Kiekviena mergaitė rankose laiko po dubenėlį, kiekviename dubenėlyje yra po dešimt slyvų.
Kai kurios mergaitės suvalgo po kelias slyvas.
Kiekviena mergaitė perduoda dubenėlį dešinėje nuo jos esančiam mokiniui. Kiekvienas mokinys,
gavęs dubenėlį, suvalgo vieną slyvą ir perduoda jį toliau į dešinę tol, kol slyvos baigiasi.
Parašykite programą, kuri apskaičiuotų, kiek slyvų suvalgė kiekvienas mokinys.

Vienoje eilutėje surašyta dešimt sveikųjų skaičių, atskirtų vienu tarpo simboliu. Šie skaičiai nusako,
kiek slyvų suvalgė kiekviena mergaitė prieš joms pradedant vaišinti kitus mokinius.

kas gauta iš kitų + (10 - pradinis sulesimas) + kiek liko padalinti po 1 į dešinę
jeigu einant paeiliui: 6 - 4 - 2 - 2 - 2 - 1 - 1 - 1 - 1

Galiausiai apsistojau ties tuo, kad kaskart tam tikru intervalu būtų pridedama po vienetą
'''
be_krepšelių = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # Sukuriamas 10 elementų ilgio sąrašas, kuris vėliau prilipdomas prie kitų.
pradinis = [6,3,2,8,0,5,4,9,1,3]              # Sąlygoje pateikiamas sąrašas
liko = []                                     # Sukuriamas tuščias sąrašas, kuriame laikomos likusių slyvų vertės
for i in pradinis:
    liko.append(10 - i)

liko += be_krepšelių                 # Sukuriamas bendras, 20 elementų ilgio sąrašas, kiek likę slyvų po pirminio pavalgymo
visi = pradinis + be_krepšelių       # Sukuriamas bendras, 20 elementų ilgio sąrašas, prie kurio verčių bus pridedama po 1

for n in range(1, len(liko)):
    for i in range(n, (n + liko[n - 1])):
        visi[i] += 1

print(visi)
