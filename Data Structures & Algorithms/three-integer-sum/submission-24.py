class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        sol = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                result = nums[i] + nums[left] + nums[right]

                if result == 0:
                    sol.append([nums[i], nums[left], nums[right]])
                    while left < len(nums) - 1 and nums[left] == nums[left + 1]:
                        left += 1
                    while right > 0 and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif result < 0:
                    left += 1
                else:
                    right -= 1
        return sol