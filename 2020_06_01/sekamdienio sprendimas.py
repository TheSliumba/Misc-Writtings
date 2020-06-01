"""
Sąlyga:
Vartotojo paprašoma įvesti eilę skaičių ir simbolių, pvz:
aa11b2C3
Užduotis:
Surinkti skaičius, atspausdinti jų sumą.
Atspausdinti listą su skaičiais išrikiuotais didėjančia tvarka
Raides atsausdinti kaip vieną string, pakeičiant mažasias didžiosiomis ir atvirkščiai.
Suskaičiuoti raidžių pasikartojimus, nekreipiant dėmesio ar tai didžioji ar mažoji raidė.
"""


def collect_nums(string: str):
    "Surinkti skaičius, atspausdinti jų sumą."
    numbers = ''
    number = 1  # Šitas skaičius naudojamas patikrint, ar prieš tai buvo skaičius.
                # Taip įsitikinam, ar tai vienženklis ar ne
    for i in string:
        if i.isdigit() and number == 1:  # Jeigu praeitame žingsnyje buvo įrašytas skaičius ir dabar vėl skaičius,
                                         # primetam, kad jis daugiaženklis, ir naują skaičių prirašom prie jo.
            numbers += i
            number = 1
        elif i.isdigit() and number == 0:
            numbers = numbers + ' ' + i  # Skaičius įrašomas su tarpu, kad atskirti su split().
            number = 1
        elif not i.isdigit():
            number = 0  # Čia baigiasi logika, kurioje išrenkami skaičiai ir surašomi į eilutę.

    numbers_final = []
    for i in numbers.split():
        if len(i) != 0:
            numbers_final.append(int(i))
    return numbers_final


def collect_letters(string: str):
    letters = ''
    for i in string:
        if i.isalpha():
            if i.isupper():
                letters += i.lower()
            else:
                letters += i.upper()
    return letters


def count_letters(string: str):
    counter = {}
    for i in string:
        if i.lower() in counter:
            counter[i.lower()] += 1
        else:
            counter[i.lower()] = 1
    return counter


line = input("Įveskite maklę\n")

"Surinkti skaičius, atspausdinti jų sumą."
print(f'Kratinyje sutinkamų skaičių suma: {collect_nums(line)}')

"Atspausdinti listą su skaičiais išrikiuotais didėjančia tvarka"
print(f'Išrikiuotas listukas: {sorted(collect_nums(line))}')

"Raides atsausdinti kaip vieną string, pakeičiant mažasias didžiosiomis ir atvirkščiai."
print(f"Surinktos raidės ir pakeistos: {collect_letters(line)}")

"Suskaičiuoti raidžių pasikartojimus, nekreipiant dėmesio ar tai didžioji ar mažoji raidė"
print(f"Suskaičiuotas paskartojimas: {count_letters(collect_letters(line))}")
