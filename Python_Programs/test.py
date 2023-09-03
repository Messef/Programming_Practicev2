class Solution:
    def maxArea(height) -> int:
        ma= 0 #max area
        st= 0 #start
        en= len(height)-1 #end
        while st< en: #while these two pointers don't interesect
            an= (min(height[st], height[en]))* (en- st) #current area
            if an> ma: #if the max area is less than the current area update the variable
                ma= an
            if height[st] < height[en]: #if the left pointer's height is less than the right pointer decrement the left one. This works to find a higher height
                st+=1
            else: #move the right pointer closer in
                en-=1
        return ma #answer