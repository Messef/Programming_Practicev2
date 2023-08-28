def reverseBits(n: int) -> int:
        ans=0
        n=[int(n) for n in str(n)]
        for x, y in enumerate(n[::-1]):
          if y==1:
            mod=2**(len(n)-x-1)
            ans+=mod
        return ans, n
print(reverseBits(0b10000010100101000001111010011100))
