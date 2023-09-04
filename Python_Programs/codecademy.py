def maxProfit(prices) -> int:
    if len(prices)==1: return 0
    prof=0
    l=0
    for x, y in enumerate(prices): 
        left=prices[l]
        print(prices, left, y, prof, (y-left))
        if y>prices[l]: 
            prof+=(y-left)
        l=x
    return prof
print(maxProfit([2, 1, 4]))