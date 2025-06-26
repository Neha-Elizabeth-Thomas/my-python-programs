f=open("numbers.txt","r")
numbers=[]
for line in f:
    try:
        numbers+=[float(x) for x in line.split(" ")]
    except ValueError:
        continue
print(numbers)

p=open("positive.txt","w")
n=open("negative.txt","w")

pos=[x for x in numbers if x>=0]
neg=[x for x in numbers if x<0]

p.write("\n".join(map(str,pos)))
n.write("\n".join(map(str,neg)))

p.close()
n.close()
f.close()