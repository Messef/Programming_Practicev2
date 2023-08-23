def isValid(s: str) -> bool:
    has={
        '{': '}',
        '[': ']',
        '(':")"
    }
    bool=True
    new_string = [str(s) for s in str(s)]
    for y in new_string:
        x=new_string.index(y)
        print(x)
        if '(' in new_string:
            if has[y] in new_string:
              new_string.remove(has[y])
              new_string[x]=='x'
            else: 
              bool= False
              break

        elif '{' in new_string:
            if has[y] in new_string:
                new_string.remove(has[y])
                new_string[x]=='x'
            else: 
              bool= False
              break
              
            
        elif '[' in new_string:
            print(has[y])
            if has[y] in new_string:
                new_string.remove(has[y])
                new_string[x]=='x'
            else: 
              bool= False
              break
        elif new_string==None:
           bool= True
           break
    return bool    
print(isValid('([)'))