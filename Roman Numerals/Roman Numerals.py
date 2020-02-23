'''
Pagaminti funkciją, kuri paimtą skaičių perrašytų romėniškais skaitmenimis.
Simbolis   Vertė
I          1
V          5
X          10
L          50
C          100
D          500
M          1,000
'''

def konvertuoti_i_roman(skaicius):
    vert = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simb = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
    roman = ''
    i = 0
    while skaicius > 0:
        for _ in range(skaicius // vert[i]):
            roman += simb[i]
            skaicius -= vert[i]
        i += 1
    return roman

def konvertuoti_i_skaiciu(romeniskas):
    #vert = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simb = {"M":1000, "CM":900, "D":500, "CD":400, "C":100, "XC":90, "L":50, "XL":40, "X":10, "IX":9, "V":5, "IV":4, "I":1}
    skaicius = 0
    i = 0
    for k in romeniskas:
        skaicius += simb[k]
        i += 1
    return skaicius


rez = konvertuoti_i_skaiciu("MDCLXIV")
print(rez)
