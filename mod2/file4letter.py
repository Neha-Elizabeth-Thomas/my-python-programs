words=[]
f=open("myfile.txt","r")

line=f.read()
words+=line.split()
    
words4=list(filter(lambda x:len(x)==4,words))
print(words4)
print(f"no of 4 letter words={len(words4)}")

f.close()