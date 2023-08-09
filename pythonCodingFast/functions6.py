import math

# Functions are simple pre-writen code that perform a certain task.

def isPrime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True

checkPrime = isPrime(int(input("Enter num: ")))
if checkPrime:
    print("Prime")
else:
    print("Not prime")    

