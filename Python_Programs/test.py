class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        l = 0
        output = 0
        for r, x in enumerate(s):
            if x not in seen:
                output = max(output,r-l+1)
            else:
                if seen[x] < l: #Find out why lines 10 and 11 are here and what they do
                    output = max(output,r-l+1)
                else:
                    l = seen[x] + 1
            seen[x] = r
        return output