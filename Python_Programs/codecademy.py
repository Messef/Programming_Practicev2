nums=[2,7,11,15]
target=9
class Solution():
    def twoSum(test, nums, target):
        test.nums=[]
        test.target=0
    def findIndicies(nums, target):
        x=0
        y=0
        while x<(len(nums)):
            while y<(len(nums)):
                if nums[x]+nums[y]==target:
                    return x, y
                    break
                else:
                    y+=1
            x+=1
test=Solution()
Solution.findIndicies(nums, target)