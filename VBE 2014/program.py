with open("u1.txt") as file:
    data = [i.strip() for i in file]
full_data = {}


def count_maxe(list):
    occs = {}
    for i in list:
        if i in occs:
            occs[i] += 1
        else:
            occs[i] = 1
    return sorted(occs.items(), key= lambda x: [x])[-1]


for i in data:
    if data.index(i)+1 != len(data):
        full_data[f'Skyrius {data.index(i)+1}'] = [int(i) for i in i.split()]
    else:
        full_data["Direktorius"] = i

points = {}
for i in data:
    if data.index(i)+1 != len(data):
        points[f'Skyrius {data.index(i)+1}'] = [0, 0, 0]
    else:
        points["Direktorius"] = [0, 0, 0]

maxes = count_maxe(full_data['Skyrius 3'])[1]
print(full_data)
print(points)
print(maxes)
