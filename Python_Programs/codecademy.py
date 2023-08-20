'''
Is an integer a palindrome?
'''
class Solution:
   def isPalindrome(x: int) -> bool:
        new_x = [str(x) for x in str(x)]
        if new_x == new_x[::-1]:
            return True, type(new_x)
        else: 
            return False
my_Solution=Solution()
print(Solution.isPalindrome(121))