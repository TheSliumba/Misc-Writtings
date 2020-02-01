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

print(3//1)