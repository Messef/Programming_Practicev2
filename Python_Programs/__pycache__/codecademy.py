#Wordle
import random
text_file = open('Python_Programs/__pycache__/file.txt','r')
line_list = text_file.readlines();
rand = random.randint(0, len(line_list))
line_list[rand] = line_list[rand].lower()
sw = 0
line_list[rand]
theWord = "steel"
theWord=line_list[rand]
theWord = theWord[0:5]
hashmap = {}
def searchFor(word) -> bool:
        it = 0
        word=word.lower()
        l=0
        r=len(line_list)
        while l < r:
            mid=(l+r) // 2
            if line_list[mid].lower()<word: 
                  l=mid+1
            else: 
                  r=mid
            it+=1
            if line_list[mid][0:5].lower() == word:
                print(f"{it} tries!")
                return True
        return False

for x in theWord: 
    if x not in hashmap:
        hashmap[x]=1
        continue
    hashmap[x]+=1
def Wordle(guessNum):
 global sw
 i=0
 while i<guessNum:
    counterhashmap = {}
    hashfin = {}
    guess=input("What is your guess(5 letters)? ")
    
    if len(guess)!=5 or searchFor(guess)==False: 
        print("guess in english dict and is 5 chars")
        print(guessNum)
        Wordle(guessNum)
    guessNum-=1
    print(guessNum)
    guess = guess.lower()
    confirmation = []
    msg=""
    for x in guess: 
        if x not in counterhashmap:
            counterhashmap[x]=1
            continue
        counterhashmap[x]+=1
    for x, y in enumerate(guess): 
        if y is not theWord[x]:
            hashfin[x] = False
            continue
        hashfin[x] = True

    for z,y in enumerate(guess): 
        if y not in theWord: 
            confirmation.append("n")
            continue
        elif y in theWord and guess[z]!=theWord[z]:
            if counterhashmap[y] > hashmap[y]:
             if sw == 0: 
                for it, ittwo in enumerate(guess):
                    sw = 1
                    if ittwo is not guess[z] and it is not z:
                        theta = it
                        break
                if guess[theta] == guess[z]:
                    confirmation.append("n")
                    continue

                confirmation.append("m")
                
                continue
             confirmation.append("n")
             continue
            confirmation.append("m")

            continue
        elif guess[z]==theWord[z]:
            if y not in counterhashmap:
                confirmation.append("y")
                continue
            confirmation.append("y")

    for ite in confirmation:
        msg+=ite
    print(msg)
    if msg == "yyyyy":
        break
 print(theWord, counterhashmap, hashmap)
 quit()
Wordle(6)


