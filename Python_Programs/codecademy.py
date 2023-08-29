def lengthOfLongestSubstring( s: str) -> int:
        seen=[]
        values=[0]
        counter=0
        for  y in s:
            if y not in seen:
                seen.append(y)
                counter+=1
            else:
                values.append(counter)
                seen=seen[seen.index(y):]
                seen.remove(y)
                seen.append(y)
                counter=len(seen)
        values.append(counter)
        return max(values)
            
            
print(lengthOfLongestSubstring("aabaab!bb"))