import math
def isPrime(num):
    if(num in [0,1]):
        return False
    
    for i in range(2,int(math.sqrt(num))+1):
        if(num%i==0):
            return False
    else:
        return True
    
low=int(input("Enter lower bound: "))
high=int(input("Enter higher bound: "))
primeNumbers=list(filter(isPrime,range(low,high+1)))
print(f"Prime numbers between {low} and {high}: ")
print(list(primeNumbers))
print(len(primeNumbers))