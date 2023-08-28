#contains duplicate
def containsDuplicate(nums: int) -> bool:
        nums=sorted(nums)
        for x, y in enumerate(nums):
            if y==nums[x-1]:
                return True
        return False
print(containsDuplicate([1, 2, 3, 4, 5, 1]))
