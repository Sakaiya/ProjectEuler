import math

def findAllFactor(number):
    factor = []
    sqrt = round(math.sqrt(number))
    for i in range(1,sqrt):
        if (number / i).is_integer():
            factor.append(i)
            factor.append(int(number / i))
    return factor

def isPrime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i *i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i = i + 6
    return True

number = 600851475143
factor =  findAllFactor(number)
nbPrime = []
for nb in factor:
    if isPrime(nb):
        nbPrime.append(nb)
nbPrime = sorted(nbPrime, reverse = True)

print(nbPrime[0])
