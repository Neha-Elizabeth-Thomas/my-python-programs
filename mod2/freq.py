str=input("Enter a string: ")
dict={}
for ch in str:
    dict[ch]=dict.get(ch,0)+1
print(dict)