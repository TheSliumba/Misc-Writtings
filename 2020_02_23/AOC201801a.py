import time

with open("input.txt") as f:
    input = list(f)
input = [i.strip() for i in input]

freq = 0


print(freq)
frequencies = {}

start_time = time.time()
searching = True

while searching:
    for i in input:
        if i[0] == "+":
            freq += int(i[1:])
        else:
            freq -= int(i[1:])
        if freq in frequencies:
            searching = False
            result = freq
            break
        else:
            frequencies[freq] = 1
print(result, f"This whole thing took only {time.time() - start_time} seconds, bro")