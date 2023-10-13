theWord = "state"
alphabet = "abcdefghijklmnopqrstuvwxyz"
hashmap = {


}
for x in theWord: 
    if x not in hashmap:
        hashmap[x]=1
        continue
    hashmap[x]+=1
print(hashmap)