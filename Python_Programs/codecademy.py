def buyChoco(prices, money) -> int:
    l=0
    r=1
    output=0
    prices=sorted(prices)
    while r < len(prices):
        sum=prices[l]+prices[r]
        if sum<=money:
           output=max(output, money-sum)
           l=r+1
        r+=1
    if l==0:
     return money
    else: 
       return output
print(buyChoco([1,2,2], 3))