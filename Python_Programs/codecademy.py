def intToRoman(num: int) -> str:
    hashmap={
            1000:'M',
            900: 'CM', 
            500: 'D',
            400:'CD',
            100:'C',
            90:'XC',
            50:'L',
            40:'XL',
            10: 'X',
            9: 'IX',
            5: 'V',
            4:'IV',
            1:'I',
            0:''
            
        }
    new_num = [int(num) for num in str(num)]
    ans=""
    x=0
    while x<len(new_num):
       math=len(new_num)-(x+1)
       new_num[x]=new_num[x]*10**math
       x+=1
    for y in new_num:
       if y in hashmap:
        ans+=hashmap[y]
       else: 
        counter=0
        for x in hashmap.keys():
          if x<y:
            while (counter+x)<=y and x!=0:
             print(x, counter, ans)
             ans+=hashmap[x]
             counter+=x
            else:
              continue
           
    return new_num, ans
print(intToRoman(112))