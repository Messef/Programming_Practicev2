def removeDuplicates(nums):
        stack=nums[0]
        counter=1
        for x, y in enumerate(nums):
         
         if x!=0:
            if y != stack:
                stack=y
                counter+=1

        return counter
print(removeDuplicates([-1,0,0,0,0,3,3]))