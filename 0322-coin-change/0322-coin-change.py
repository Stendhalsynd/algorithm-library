class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0

        INVALID = 10001

        memo = [INVALID] * (amount + 1)
        memo[0] = 0

        for coin in coins:
            for idx in range(coin, len(memo)):
                if memo[idx - coin] != INVALID:
                    memo[idx] = min(memo[idx], memo[idx - coin] + 1)

        return memo[amount] if memo[amount] != INVALID else -1