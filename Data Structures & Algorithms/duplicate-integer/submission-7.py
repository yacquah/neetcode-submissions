class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # store values we have seen 
        # loop through
        # if curr is seen, then return false
        # at the end of the loop return True

        seen = set()

        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False
