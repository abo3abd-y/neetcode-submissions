class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count = 0
        sum_far = 0

        for i in range(0, k):
            sum_far += arr[i]
        if sum_far/k >= threshold:
            count += 1
        for j in range(i + 1, len(arr)):
            sum_far += arr[j]
            sum_far -= arr[j-k]
            if sum_far/k >= threshold:
                count += 1
        return count


        
