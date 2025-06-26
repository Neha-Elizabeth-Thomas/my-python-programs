def findNum(numstr,base):
    exp=len(numstr)-1
    num=0
    for dig in numstr:
        dig=int(dig)
        num+=dig*base**exp
        exp-=1
    return num

num=input("Enter a  number: ")
base=int(input("base: "))
print(findNum(num,base))