class Solution:
    def isValid(self, s: str) -> bool:
        # to know if there are true paranthesis, you need to use stacks
        open_brackets = {'(', '[', '{'}
        close_brackets = {')', ']', '}'}
        stack = []
        for char in s:
            if char in open_brackets:
                stack.append(char)
            elif len(stack) == 0:
                stack.append(' ')
                break
            elif char in close_brackets:
                popped = stack[-1]
                if not ((popped == '(' and char == ')') or (popped == '[' and char == ']')
                or (popped == '{' and char == '}')):
                    break
                else:
                    stack.pop()
        return len(stack) == 0
            