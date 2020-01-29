import numpy as np

## For Part One
data = np.loadtxt('day1-a_data.txt', dtype=int)

fuel = np.sum(np.subtract(np.floor(data / 3), 2.0))

print(fuel)

## Part 2
fuel = 0
for x in data:
    fuel_calc = x
    while True:
        fuel_calc = int(fuel_calc / 3) - 2
        if fuel_calc < 0:
            break
        else:
            fuel += fuel_calc

print(fuel)
