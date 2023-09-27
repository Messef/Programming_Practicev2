def factors():
    num = int(input("enter a num: "))
    num2 = int(input("enter another num: "))
    target = int(input("enter a target int: "))
    num*=num2
    x= -abs(num//2)
    while x <=abs(num)//2:
        if x==0: 
            x+=1
            continue
        elif num % x ==0: 
            if x+(num/x) == target:
                return x, int(num/x)
        x+=1
    return "none"
print(factors())