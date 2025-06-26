import math
x=float(input("Enter x: "))
n=int(input("How many terms: "))

sum=0
for i in range(n):
    term=x**i/math.factorial(i)
    sum+=term
    
print(sum)
print(math.exp(x))

