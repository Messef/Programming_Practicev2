def maxProfit(prices) -> int:
    if (len(prices))==1: return 0
    l=0
    output=0
    for x, y in enumerate(prices):
     left=prices[l]
     if left>=y:
        l=x
     else:
        output = max(output, (y-left))
    return output
print(maxProfit([7,1,5,3,6,4]))