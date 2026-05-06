class Solution:
    def isValid(self, s: str) -> bool:
        # to know if there are true paranthesis, you need to use stacks
        open_brackets = {'(', '[', '{'}
        close_brackets = {')', ']', '}'}
        stack = []
        stack.append(s[0])
        iterator = 1
        while iterator < len(s):
            if s[iterator] in open_brackets:
                stack.append(s[iterator])
            elif len(stack) == 0:
                stack.append('lost')
                break
            elif s[iterator] in close_brackets:
                popped = stack[-1]
                if not ((popped == '(' and s[iterator] == ')') or (popped == '[' and s[iterator] == ']')
                or (popped == '{' and s[iterator] == '}')):
                    break
                else:
                    stack.pop()
            iterator += 1
        return len(stack) == 0
            