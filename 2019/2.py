#!/usr/local/bin/python3
import math

def calculateRecursiveFuel(massValue):
    calculatedFuel = calculateFuel(massValue)
    totalFuel = calculatedFuel
    while calculateFuel(calculatedFuel) > 0:
        calculatedFuel = calculateFuel(calculatedFuel)
        totalFuel += calculatedFuel
    return totalFuel

def calculateFuel(mass):
    return math.floor(mass / 3) - 2

totalFuel = 0
f = open('2.txt')
for mass in f:
    totalFuel += calculateRecursiveFuel(int(mass))
print("totalFuel = " + str(totalFuel))

# print(30, calculateRecursiveFuel(30)) #18
# print(60, calculateRecursiveFuel(60)) #22
# print(14, calculateRecursiveFuel(14)) #2
