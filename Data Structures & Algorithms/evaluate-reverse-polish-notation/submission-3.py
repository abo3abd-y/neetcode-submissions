class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            try:
                stack.append(int(token))
            except ValueError:
                if len(token) > 1:
                    stack.append(int(token[1:]))
            
                else:
                    first = int(stack.pop())
                    second = int(stack.pop())
                    if token == '+':
                        result = second + first
                    elif token  == '-':
                        result = second - first
                    elif token == '*':
                        result = second * first
                    else:
                        result = int(second / first)
                    stack.append(result)
        return stack[0]