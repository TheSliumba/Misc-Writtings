'''
Ūkininkas išspaustą aliejų išpilsto į turimus vieno litro, trijų litrų ir penkių litrų indus. Pirmiausia
aliejus pilamas į penkių litrų indus. Po to, jeigu reikia, – į trijų litrų indus, galiausiai, jeigu reikia, – į
vieno litro indus. Nepilnai užpildyto indo neturi būti. Indų aliejui pilstyti gali būti pakankamai, per daug
arba per mažai.
Parašykite programą, kuri suskaičiuotų:
 kiek buvo pripilta turimų vieno, trijų ir penkių litrų indų ir kiek litrų aliejaus liko neišpilstyta;
 kiek vieno, trijų ir penkių litrų indų papildomai reikėtų įsigyti, norint tuo pačiu būdu išpilstyti visą
likusį aliejų;
 koks bus gautas pelnas, pardavus visus indus su aliejumi; visų indų kainos įskaičiuotos į aliejaus
gamybos išlaidas.
'''

with open('2019_1_T.txt') as f:
    data = [l.strip() for l in f]

def calculate_initial(data):
    total_oil = int(data[0].split()[3])
    ones, threes, fives = int(data[0].split()[0]), int(data[0].split()[1]), int(data[0].split()[2])
    manufacture_cost, ones_sale, threes_sale, fives_sale = int(data[1].split()[0]), \
                                                           int(data[1].split()[1]), \
                                                           int(data[1].split()[2]), \
                                                           int(data[1].split()[3])

    containers = {5: fives, 3: threes, 1: ones}
    used_containers = {5: 0 , 3: 0, 1: 0}
    selling = {5:fives_sale, 3: threes_sale, 1: ones_sale}

    for k,v in containers.items():
        for _ in range(v):
            if total_oil // k > 0:
                total_oil -= k
                used_containers[k] += 1
            else:
                continue

    leftover_oil = total_oil
    required_containers = {5: 0, 3: 0, 1: 0}

    while leftover_oil > 0:
        for k in required_containers.keys():
            required_containers[k] = leftover_oil // k
            leftover_oil -= (leftover_oil // k) * k

    total_containers = {}
    for i in containers:
        total_containers[i] = containers[i] + required_containers[i]

    total_profit = 0
    for i in total_containers:
        total_profit += total_containers[i] * selling[i]

    total_profit -= manufacture_cost

    return f" Iš viso liko: {total_oil}, Panaudota litrinių: {used_containers[1]}, " \
           f"Panaudota trilitrių: {used_containers[3]}, Panaudota penkialitrių: {used_containers[5]}, " \
           f"Pritrūko pagal litražą: 5L-{required_containers[5]}, 3L-{required_containers[3]}," \
           f"1L-{required_containers[1]}, Pelnas: {total_profit}"

print(calculate_initial(data))