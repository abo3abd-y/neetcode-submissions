class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dupl = set()

        left = right = 0
        size = len(s)
        max_sub = 0
        while right < size:
            if s[right] not in dupl:
                dupl.add(s[right])
                right += 1
                max_sub = max(max_sub, right - left)
            else:
                dupl.remove(s[left])
                left += 1
        return max_sub

