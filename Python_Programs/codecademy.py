nums1=[1, 2]
nums2=[3, 4]
def findMedianSortedArrays(nums1=[], nums2=[]) -> float:
        x=0
        nums1.extend(nums2)
        nums1.sort()
        while len(nums1)>2:
            nums1.pop(x)
            nums1.pop(-(x+1))
        if len(nums1)==1:
            return nums1
        else:
            return (nums1[0]+nums1[1])/2
print(findMedianSortedArrays(nums1, nums2))