def factors(num, num2,target):
    x=2
    num*=num2
    stack=[num]
    hashmap={}
    while x <=num/2:
        if num%x==0:
            stack.append(x)
        x+=1
    for x,y in enumerate(stack):
        hashmap[y] = x
    for x,y in enumerate(stack):
        complement=target - y
        if complement in hashmap.keys()and hashmap[complement] != x:
            return stack[x], (target-stack[x])
    return "none"
print(factors(4, -27, -18))

