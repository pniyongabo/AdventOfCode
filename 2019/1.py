#!/usr/local/bin/python3
import math

totalFuel = 0
#n = 0
f = open('1.txt')
for mass in f:
    fuel = math.floor(int(mass) / 3) - 2
    #n += 1
    totalFuel += fuel
    #print (n, totalFuel)
print("totalFuel = " + str(totalFuel))
