import numpy as np

## For Part One
data_init = (np.loadtxt('day2_data.txt', dtype=int, delimiter=','))
data = data_init

key = 19690720
data[1] = 12
data[2] = 2

i = 0
while True:
    if data[0] == 19690720:
        break
    elif data[i] == 1:
        j1 = data[i + 1]
        j2 = data[i + 2]
        j3 = data[i + 3]
        data[j3] = data[j1] + data[j2]
        i += 4
    elif data[i] == 2:
        j1 = data[i + 1]
        j2 = data[i + 2]
        j3 = data[i + 3]
        data[j3] = data[j1] * data[j2]
        i += 4
    elif data[i] == 99:
        break

print(data)


