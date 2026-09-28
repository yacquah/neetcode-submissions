class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()
        maxL = 0
        curMax = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            currMax = max(curMax, r-l+1)
            maxL = max(maxL, currMax)
            r += 1
            
            

        return maxL


            
