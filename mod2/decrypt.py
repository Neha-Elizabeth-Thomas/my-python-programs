cipher=input("Ente cipher: ").lower()
d=int(input("Enter offset: "))
plain=""
for ch in cipher:
    p=ord(ch)-d
    if  p<ord('a'):
        p=ord('z')-(ord('a')-p)+1
    plain+=chr(p)
    
print(plain)
    