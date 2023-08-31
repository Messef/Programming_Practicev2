def rearrangeCharacters(s: str, target: str) -> int:
    target=sorted(target)
    stack=""
    s=sorted(s)
    output =1000
    r=0
    l=0
    for x in s:
        if x in target:
            if stack != "" and x!=stack[-1]:
                output=min(output, r-l+1)
                l=r
                output=r-l+1
            stack+=x
            r+=1
        print(output, r, l, stack, stack[-1], x)
    if target[-1] in stack:
        return output
    return 0
print(rearrangeCharacters("ilovecodingonleetcode", "code")) 
                
          