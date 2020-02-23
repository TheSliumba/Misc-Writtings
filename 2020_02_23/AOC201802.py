
with open("checksum.txt") as f:
    input = list(f)
input = [i.strip() for i in input]

count_of_twos: int = 0
count_of_threes = 0
count_of_both = 0

for i in input:
    dicc = {}
    for k in i:
        if k in dicc:
            dicc[k] += 1
        else:
            dicc[k] = 1
    if 2 in dicc.values():
        count_of_twos += 1
    if 3 in dicc.values():
        count_of_threes += 1

print(count_of_threes*count_of_twos)