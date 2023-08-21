def repeatedSubstringPattern(s):
    x=0
    original=s
    substring=original[0:x+1]
    while substring in original and x<5:
        substring=original[0:x+1]
        s=original.replace(substring, "")
        print(s, substring, x)
        x+=1
    
    else:
        if type(len(original)/len(substring))==int:
            return substring
        else:
            print('fail')
            print( substring, s, original, x)
    
repeatedSubstringPattern("abcabcabc")