nums =[-1, 0, 5, 6, 6, 7, 8, 8, 9]
def removeDuplicates(nums) -> int:
  j = 1
  for i in range(1, len(nums)):
    print(nums, nums[j], nums[i])
    if nums[i] != nums[i - 1]:
        print(nums)
        nums[j] = nums[i]
        j += 1
  return j, nums
print(removeDuplicates(nums))