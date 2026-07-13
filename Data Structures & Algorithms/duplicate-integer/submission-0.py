class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     # if list is empty return False
     # check if num is in seen
     # if it is then return True, else add to seen
        if not nums:
            return False
        
        seen = []
        for num in nums:
            if num in seen:
                return True
            else:
                seen.append(num)
                continue
        return False