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
    guess=input("What is your guess(5 letters)? ")
    if len(guess)!=5: 
        break
    guess = guess.lower()
    confirmation = []
    msg=""
    for x in guess: 
        if x not in counterhashmap:
            counterhashmap[x]=1
            continue
        counterhashmap[x]+=1
    for x,y in enumerate(guess): 
        if y not in theWord: 
            confirmation.append("n")
            continue
        elif y in theWord and guess[x]!=theWord[x]:
            if counterhashmap[y] > hashmap[y]:
                confirmation.append("n")
                continue
            confirmation.append("m")

            continue
        elif guess[x]==theWord[x]:
            if y not in counterhashmap:
                confirmation.append("y")
                continue
            confirmation.append("y")

    for x in confirmation:
        msg+=x
    print(msg)
    if msg == "yyyyy":
        break
print(theWord)

