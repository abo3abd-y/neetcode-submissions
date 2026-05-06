class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # stores the indices and not the actual values
        result = [0] * len(temperatures)
        for idx in range(len(temperatures)):
            stack.append(idx)
            while len(stack) > 1 and temperatures[stack[-1]] > temperatures[stack[-2]]:
                result[stack[-2]] = stack[-1] - stack[-2]
                temp = stack.pop()
                stack.pop()
                stack.append(temp)
        return result