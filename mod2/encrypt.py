str=input("Enter message: ").lower()
d=int(input("Enter offset: "))
cipher=""
for ch in str:
    e=ord(ch)+d
    if e>ord('z'):
        e=ord('a')+e-ord('z')-1
    cipher+=chr(e)
    
print(cipher)