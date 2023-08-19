word="chess"
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
def find_unique_letters(word):
    #Fast way (doesn't work if word has non-alphabetic characters)
    '''
    wordSet = set(word)
    return len(wordSet)
    '''
    uniqueSet = set(letters)
    count = 0
    for char in word:
        if char in uniqueSet:
            count+=1
            uniqueSet.remove(char)

    return count
def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques




print(find_unique_letters(word))