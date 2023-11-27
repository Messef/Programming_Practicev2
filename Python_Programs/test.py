rep = ""
for i in range(16):
        for x in range(30):
            
            if i*30+x < 10:
                  rep += f"| 00{30*i+x} |"
            elif i*30+x<100:
                  rep += f"| 0{30*i+x} |"
            else: 
                  rep += f"| {30*i+x} |"
                  
        rep+="\n"
print(rep)