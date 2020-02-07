import numpy as np

# For Part One
data_init = np.loadtxt('day2_data.txt', dtype=int, delimiter=',')
data = data_init

key = 19690720

for noun in range(0, 100):
    for verb in range(0, 100):
        data = data_init.copy()
        data[1] = noun
        data[2] = verb
        i = 0
        while True:
            if data[i] == 1:
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
        if data[0] == key:
            print('noun: ', noun)
            print('verb: ', verb)
            print('answer: ', (100 * noun + verb))
            exit()