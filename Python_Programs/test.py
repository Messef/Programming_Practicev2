#contains duplicate
def containsDuplicate(nums: int) -> bool:
        if len(nums)==len(set(nums)):
           return False
        return True
print(containsDuplicate([1, 2, 3, 4, 5, 1]))
