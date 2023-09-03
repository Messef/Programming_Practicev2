def maxArea(height):
    dist=1
    output=0
    left=0
    right=1
    while right<len(height):
        nums=min(height[left], height[right])
        nums*=dist
        output=max(nums, output)
        if height[left]<height[right]:
            left=right
            dist=0
        dist+=1; right+=1
    return output
print(maxArea([1,2,1]))
