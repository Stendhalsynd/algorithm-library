class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        
        memo = [0] * (n + 1)
        memo[1] = 1
        memo[2] = 2

        def dp(n):
            if memo[n] != 0:
                return memo[n]
            memo[n] = dp(n - 2) + dp(n - 1)
            return memo[n]

        return dp(n)