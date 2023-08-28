'''Example 1:

Input: n = 00000010100101000001111010011100
Output:    964176192 (00111001011110000010100101000000)
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 
43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.'''
def reverseBits(n: str) -> int:
    ans=0
    for x, y in enumerate(n[::-1]):
     if y=="1":
      mod=2**(len(n)-x-1)
      ans+=mod
    return ans, n
print(reverseBits("00000010100101000001111010011100"))