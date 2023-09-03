def mySqrt(x: int) -> int:
    l=1
    r= x // 2
    while l<=r:
        mid = (l+r) // 2
        print(l, mid, r)
        if mid**2>x:
            r=mid-1
        elif mid**2<x:
            l=mid+1
        else: 
            return mid
    return r

print(mySqrt(8))
