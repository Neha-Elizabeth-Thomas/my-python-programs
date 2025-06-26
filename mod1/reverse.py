num=int(input("ENter a number: "))
dup=num

rev=0
while(num!=0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
    
print(f"REversed number: {rev}")
if(rev==dup):
    print("Palindrome")
else:
    print("Not palindrome")