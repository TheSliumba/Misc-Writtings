with open('skaiciai.txt') as f:
    data = [line.strip().split() for line in f]

data_b = []
op_count = 0

for i in data:
    for k in i:
        data_b.append(float(k))
    op_count += 1

print(f"Made {op_count} bigger for cycles")

print(f'Final result equates to {sum(data_b):.02f}')


def sort_out(mess: list = None):
    """

    :param mess: put in a list of lists bruh
    :return: a list of two beautiful lists of sortedness
    """

    floaters = []
    numbers = []

    for array in mess:
        for number in array:
            try:
                numbers.append(int(number))
            except ValueError:
                floaters.append(float(number))

    return numbers, floaters


print(len(data_b), len(data[0]))

result = list(sort_out(data))

print(len(result[0]))