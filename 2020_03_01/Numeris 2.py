from datetime import datetime

with open("duomenys2.txt") as f:
    data = [line.strip() for line in f]

time = {}



print(data[15].split()[4], data[15].split()[2])
for i in data:
    if i.split()[0] not in time:
        time[i.split()[0]] = 0
    else:
        #time[i.split()[0]] += ((int(i.split()[4][:2])*60 + int(i.split()[4][3:])) -
        #                       (int(i.split()[2][:2])*60 + int(i.split()[2][3:])))
        atvyko_h = int(i.split()[2][:2])
        atvyko_min = int(i.split()[2][3:])
        atvyko = (atvyko_h * 60) + atvyko_min

        isvyko_h = int(i.split()[4][:2])
        isvyko_min = int(i.split()[4][3:])
        isvyko = (isvyko_h * 60) + isvyko_min

        isbuvo = isvyko - atvyko

        time[i.split()[0]] += isbuvo

print(f'id| laikas, valandomis')
for k,v in time.items():
    print(f"{k}| {v:.02f}")


