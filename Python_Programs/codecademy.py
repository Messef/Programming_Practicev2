def romanToInt(s: str) -> int:
    roman={
        "I": 1, 
        "V": 5,
        "X": 10,
        "L": 50, 
        "C": 100,
        "D": 500,
        "M": 1000
    }
    final_int=0
    y=0
    while y<len(s):
        if y<len(s)-1:
         if roman[s[y:y+1]]<roman[s[y+1:y+2]]:
            final_int+=roman[s[y+1:y+2]]-roman[s[y:y+1]]
            y+=2         
         else:
             final_int+=roman[s[y:y+1]]
             y+=1
        else:     
            final_int+=roman[s[y:y+1]]
            y+=1
      
    return final_int

print(romanToInt(''))