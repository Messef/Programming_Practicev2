def divide(dividend: int, divisor: int) -> int:
    counter = 0
    store_dividend = dividend
    store_divisor = divisor
    dividend = abs(dividend)
    divisor = abs(divisor)
    while dividend >= divisor: 
        dividend-=divisor
        counter+=1
    if store_dividend * store_divisor <0: return (counter-2*counter)
    else: return counter
print(divide(1000000000, -3))