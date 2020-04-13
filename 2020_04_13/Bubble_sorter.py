def bubble_asc(numbers: list):  # sort out a given list of integers lowest to highest
    repeat = True
    while repeat:
        i = 0
        count = 0
        for _ in range(len(numbers) - 1):
            if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                count += 1
            i += 1
        if count == 0:
            repeat = False
    return numbers


def bubble_dsc(numbers: list):  # sort out a list of integers highest to lowest
    repeat = True
    while repeat:
        i = 0
        count = 0
        for _ in range(len(numbers) - 1):
            if numbers[i] < numbers[i+1]:
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
                repeat = True
                count += 1
            i += 1
        if count == 0:
            repeat = False
    return numbers


data = [3, 1, 4, 2, 5, 7, 9, 10, 6, 8, 12, 642, 673, 666, 3214, 23, 54, 23]


print(bubble_dsc(data))
