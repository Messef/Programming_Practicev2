def radicand(): 
    number = int(input("enter a num: "))
    sqr = 2
    max = 1
    while (sqr**2) <= number: 
        if number % (sqr**2) == 0:
            max = sqr
        sqr+=1
    number/=(max**2)
    if max == 1: return "can't be factored"
    elif number != 1: return f"{max} rad({int(number)})"  
    else: return max
print(radicand())