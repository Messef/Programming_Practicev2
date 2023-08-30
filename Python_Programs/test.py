def buyChoco(prices, money) -> int:
    prices=sorted(prices)
    if prices[0]+prices[1]<=money:
        return money-(prices[0]+prices[1])
    else: return money
print(buyChoco([4, 12, 9, 1, 2], 3))