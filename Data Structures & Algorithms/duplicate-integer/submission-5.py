class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

     # if list is empty return False
     # check if num is in seen
     # if it is then return True, else add to seen
        if not nums:
            return False
        
        seen = set()

        for i in range(len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
        return False
