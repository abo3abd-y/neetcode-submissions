class Solution:
    def decodeString(self, s: str) -> str:
        stack =  []
        for char in s:
            stack.append(char)
            if stack[-1] == ']':
                letter_repeated = ''
                digit_repeated = ''
                stack.pop()
                while stack and stack[-1] != '[':
                    if stack[-1].isalpha():
                        letter_repeated = stack.pop() + letter_repeated
                stack.pop()
                # this is the integer part where we need to consider multiple digit numbers instead of single digit numbers
                while stack and stack[-1].isdigit():
                    digit_repeated = stack.pop() + digit_repeated
                digit_repeated = int(digit_repeated)
                stack.append(digit_repeated * letter_repeated)
        return ''.join(stack)