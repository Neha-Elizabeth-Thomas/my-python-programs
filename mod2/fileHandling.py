f=open("numbers.txt","r")
p=open("positive.txt","w")
n=open("negative.txt","w")

for line in f:
    try:
        num=float(line.strip())
        if num>=0:
            p.write(str(num)+"\n")
        else:
            n.write(str(num)+"\n")
    except(ValueError):
        print("Not a number in file")
        
f.close()
p.close()
n.close()