import bisect

class Solution:
    def searchInsert(self, nums, target: int) -> int:
        return bisect.bisect_left(nums, target)