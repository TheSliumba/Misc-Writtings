from random import randint

class Kalkane:
    def __init__(self, data:list=None):
        self.data = data

    def append(self, other:int):
        return self.data.append(other)

def generate_list_of_random_values(length:int):
    values = []
    for i in range(length):
        values.append(randint(0,800))
    return values

kal = Kalkane(generate_list_of_random_values(50))
print(kal.data)