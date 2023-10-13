#Wordle
theWord = "state"
alphabet = "abcdefghijklmnopqrstuvwxyz"
hashmap = {


}
for x in theWord: 
    if x not in hashmap:
        hashmap[x]=1
        continue
    hashmap[x]+=1
for i in range(6):
    counterhashmap = {

    }
    marker = []
    guess=input("What is your guess(5 letters)? ")
    guess = guess.lower()
    confirmation = []
    msg=""
    for x,y in enumerate(guess): 
        if y not in theWord: 
            confirmation.append("n")
            continue
        elif y in theWord and guess[x]!=theWord[x]:
            if y not in counterhashmap:
                counterhashmap[y]=1
                marker.append(x)
                continue
            counterhashmap[y]+=1
            if counterhashmap[y]>hashmap[y]:
                confirmation.append("n")
                continue
            marker.append(x)
            continue
        elif guess[x]==theWord[x]:
            if y not in counterhashmap:
                counterhashmap[y]=1
                confirmation.append("y")
                continue
            counterhashmap[y]+=1
            confirmation.append("y")
            continue
    if len(marker)>0:
        for x in marker: 
            conf=marker[x]
            print(x, marker, conf)
            if counterhashmap[guess[conf]] > hashmap[guess[conf]]:
                confirmation.insert(conf, "n")
                continue
            confirmation.insert(conf, "m")
    for x in confirmation:
        msg+=x
    print(msg)
    if msg == "yyyyy":
        break




