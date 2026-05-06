class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dup = set()
        dic = {}
        answer = []

        for i in range(len(nums)):
            if (target - nums[i]) in dup:
                answer = [dic[target - nums[i]],i]
                break
            else:
                dup.add(nums[i])
                dic[nums[i]] = i
        return answer