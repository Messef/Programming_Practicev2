def factors():
    num = int(input("enter a num: "))
    num2 = int(input("enter another num: "))
    target = int(input("enter a target int: "))
    num*=num2
    x= -abs(num//2)
    stack=[num, -num]
    hashmap={}
    while x <=abs(num)//2:
        if x==0: 
            x+=1
            continue
        if num%x==0 and x not in stack:
            stack.append(x)
            stack.append(int(num/x))
        x+=1
    for x,y in enumerate(stack):
        hashmap[y] = x
    for x,y in enumerate(stack):
        complement=target - y
        if complement in hashmap.keys()and hashmap[complement] != x:
            if stack[x]*(target-stack[x])==num: 
                return stack[x], (target-stack[x])
    return "none"
print(factors())