class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        unique_values = defaultdict(int) # dictionary: value : [indices]
        result = []
        result_uniqueness = set()
        for i in range(len(nums)):
            unique_values[nums[i]] += 1
        

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):

                third = -(nums[i] +nums[j])
                zero = sorted([third, nums[i], nums[j]])
                if third in unique_values and tuple(zero) not in result_uniqueness:
                    # three all values the same
                    # two values are the same
                    # all unique
                    all_values_same = ((third == nums[i]) and (third == nums[j]) and unique_values[third] > 2)
                    print(f"all_values_same : {all_values_same}")
                    two_values_same = (((third == nums[i]) or (third == nums[j])) and (unique_values[third] > 1))
                    print(f"two_values_same : {two_values_same}")
                    all_unique = ((third != nums[i]) and (third != nums[j]))
                    print(f"all_unique : {all_unique}")
                    if (all_values_same and two_values_same) or all_unique:
                        result.append(zero)
                        print(nums[i], nums[j], third)
                        result_uniqueness.add(tuple(zero))
                    
        return result

        

        
        