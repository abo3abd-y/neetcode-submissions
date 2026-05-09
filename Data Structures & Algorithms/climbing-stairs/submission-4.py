class Solution:
    def climbStairs(self, n: int) -> int:
        fibonacci_lst = [-1] * (n+1)
        fibonacci_lst[0] = fibonacci_lst[1] = 1
        for i in range(2, n + 1):
            fibonacci_lst[i] = fibonacci_lst[i - 1] + fibonacci_lst[i - 2]
        return fibonacci_lst[n]