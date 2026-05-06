class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_set = set()
        max_length = 0
        acc = 0
        left = 0
        right = 0
        while left < len(s) and right < len(s):
            if s[right] in unique_set:
                max_length = max(max_length, acc)
                unique_set.discard(s[left])
                acc -= 1
                left += 1
            else:
                unique_set.add(s[right])
                acc += 1
                right += 1
        max_length = max(max_length, acc)
        return max_length


