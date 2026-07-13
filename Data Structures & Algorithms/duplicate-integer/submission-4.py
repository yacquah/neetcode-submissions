class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
     # if list is empty return False
     # check if num is in seen
     # if it is then return True, else add to seen
        if not nums:
            return False
        
        nums = sorted(nums)
        
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
