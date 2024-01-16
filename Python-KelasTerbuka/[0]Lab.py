import math as mt
total = 0
for i in range(0,3):
    y = i**3 / mt.factorial(i)
    total += y
print(total)
    