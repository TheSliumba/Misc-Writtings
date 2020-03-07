import random

skaiciai = [random.randint(1,1000) for _ in range(100)]
gruppe = {"Lyginiai": [], "Nelyginiai": []}
for i in skaiciai:
    if i %2 == 0:
        gruppe['Lyginiai'].append(i)
    else:
        gruppe["Nelyginiai"].append(i)
print(gruppe)
suma_lyg = sum(gruppe["Lyginiai"])
suma_nelyg = sum(gruppe["Nelyginiai"])
print(suma_lyg, suma_nelyg)
did_lyg = max(gruppe["Lyginiai"])
did_nelyg = max(gruppe["Nelyginiai"])
gruppe['Lyginiai'] = sorted(gruppe["Lyginiai"])
gruppe['Nelyginiai'] = sorted(gruppe["Nelyginiai"])
lyginiai = [str(v) for v in gruppe["Lyginiai"]]
nelyginiai = [str(v) for v in gruppe["Nelyginiai"]]
raides = 'ABCDEFGHIJ'
skaiciukai = '0123456789'
keitimas = {k:v for k,v in zip(skaiciukai, raides)}
lygraid = [keitimas[sk] for sk in skc for skc in lyginiai]
print(lyginiai)
print(lygraid)
