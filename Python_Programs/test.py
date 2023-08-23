nums=[3,2,2,3]
def removeElement(val, nums=[]) -> int:
        
        while val in nums:
            nums.pop(nums.index(val))
        k=len(nums)
        return k, nums
print(removeElement(3, nums))