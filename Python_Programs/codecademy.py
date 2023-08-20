'''
Solution to the two sum problem
'''
nums=[2, 6, 7, 11, 10]
def twoSum(nums, target: int):
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement], hashmap] 
print(twoSum(nums, 9))