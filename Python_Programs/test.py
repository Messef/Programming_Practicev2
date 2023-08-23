def isValid(s: str) -> bool:
    has={
        '{': '}',
        '[': ']',
        '(':")"
    }
    stack=[]
    for x in s:
     if x in has.keys():
      stack.append(x)
     elif x in has.values():
        if x!=has[stack.pop(-1)]:
         return False
        else:
         continue
    return len(stack)==0
print(isValid('[)]('))