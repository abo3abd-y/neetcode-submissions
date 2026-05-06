class Solution:
    def isPalindrome(self, s: str) -> bool:
        edited = s.lower().replace(" ", "")
        new_string = re.sub(r"[^a-z0-9]", "", edited)
        left = 0
        right = len(new_string) - 1
        while left < right:
            if new_string[left] == new_string[right]:
                left += 1
                right -= 1
            else:
                return False
        return True