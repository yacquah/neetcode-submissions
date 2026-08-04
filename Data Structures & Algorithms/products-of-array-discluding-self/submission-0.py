class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # loop through the list
        # for num in nums
        # initialize an ouput list
        # output[i] == product of everything except nums[i]
        
        n = len(nums)
        output = [1] * n
        
        prefix = 1
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        suffix = 1
        for i in range(n-1, -1, -1):
            output[i] *= suffix
            suffix *= nums[i]

        return output
            



        