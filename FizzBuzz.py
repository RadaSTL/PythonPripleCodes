import math

def isPrmie(val):
    #If a number n is not a prime, it can be factored into two factors a and b, n = a*b. If a number n is not a prime, it can be factored into two factors a and b: n = a * b Now a and b can't be both greater than the square root of n, since then the product a * b would be greater than sqrt(n) * sqrt(n) = n. So in any factorization of n, at least one of the factors must be smaller than the square root of n, and if we can't find any factors less than or equal to the square root, n must be a prime.
    i = 2
    if val>1:
        while i <= int(math.sqrt(val)):
            if(val%i==0):
                return False
            else:
                i += 1
        return True
    else:
        return False


for i in range(1,101):
    if isPrmie(i):
        print("Prmie")
    elif (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)
