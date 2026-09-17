class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # initialize a hashmap to hold value and index pairs
        vault = {}

        # check our domain to see if its counterpart is in the vault
        for i, num in enumerate(nums):
            num2 = target - num
            
            if num2 in vault:
                return [vault[num2],i]
            else:
                vault[num] = i