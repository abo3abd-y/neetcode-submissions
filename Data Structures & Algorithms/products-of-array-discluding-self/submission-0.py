class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        multiplier = 1
        result = [0] * len(nums)

        for i in range(len(nums)):
            result[i] = multiplier
            multiplier *= nums[i]
        multiplier = 1
        for i in range(len(nums) - 1, -1, -1):
            print(nums[i])
            result[i] *= multiplier
            multiplier *= nums[i]
        return result