def main():
    x=float(input("Enter x: "))
    y=int(input("Enter y: "))
    z=add(x,y)
    print(f"sum={z:,}") #formatted string
    print(f"a squared={square(z):.2f}")

def add(a,b):
    return a+b

def square(a):
    return a*a #a**2
#pow(a,2)

def hello(name="world"): #pass default value
    print("hello ",name)

def roundof(num):
    return round(num,2) #2nd arg optional

main()