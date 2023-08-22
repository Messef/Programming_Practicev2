def isPalindrome(x: int) -> bool:
        new_x = [str(x) for x in str(x)]
        if new_x == new_x[::-1]:
            return True, new_x
        else: 
            return False
print(isPalindrome(12344321))