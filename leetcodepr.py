nums=input()
nums=nums[1:-1]
nums=nums.split(",")
numlength=len(nums)
nums=set(nums)


newlen=len(nums)
nums=list(nums)
nums.sort()
for i in range(0,len(nums)-1):
    nums[i]=int(nums[i])
for i in range(numlength-newlen):
    nums.append("_")
    print("append")
    