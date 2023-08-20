def count_char_x(word, x):
  counter=0
  letter=0
  while letter<len(word):
    if word[letter]==x:
      counter+=1
      letter+=1
    else: 
      letter+=1
      continue
  else: 
    return counter

print(count_char_x("apple", "p"))