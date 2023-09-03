class Solution(object):
    def isHappy(self, n):
        hset = set() # no duplicates
        while n != 1: # continue 
            if n in hset: return False # if it starts to loop around - shown by if it's in the set in the first place
            hset.add(n) # add n into the set
            n = sum([int(i) ** 2 for i in str(n)]) # sum everything together using this method
        else:
            return True #after getting it to equal 1, return True