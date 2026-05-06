class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        counter  = 0
        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
            else:
                stack.append([char, 1])
            if stack and stack[-1][1] == k:
                stack.pop()
        return "".join(t[0] * t[1] for t in stack)
                  