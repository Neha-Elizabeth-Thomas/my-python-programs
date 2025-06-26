from functools import reduce
def mean(nums):
    sum=reduce(lambda x,y:x+y,nums)
    return sum/len(nums)

def median(nums):
    nums.sort()
    if(len(nums)%2==1):
        return nums[len(nums)//2]
    else:
        avg=(nums[len(nums)//2]+nums[len(nums)//2-1])/2
        return avg
        
def mode(nums):
    dict={}
    for num in nums:
        if num  not in dict:
            dict[num]=nums.count(num)
    return max(dict,key=dict.get)

myList=[1,1,1,2,3,4,6,6,6]
print(mean(myList))
print(mode(myList))
print(median(myList))