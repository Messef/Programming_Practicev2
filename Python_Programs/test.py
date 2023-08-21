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
        previous = roman[s[y]]
        next = roman[s[y+1]]
        if y<len(s)-1:
            if previous<next:
                final_int+=next-previous
                y+=2         
            else:
                final_int+=previous
                y+=1
        else:     
            final_int+=previous
            y+=1
      
    return final_int

print(romanToInt('MCMXCIV'))