import math

def smallestMultiple(number):
    mult = []
    for i in range (1,21):
        if number % i != 0:
            return False
    return True
number = 21
while(not smallestMultiple(number)):
    number += 1
print(number)
