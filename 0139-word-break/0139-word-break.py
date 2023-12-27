# 09:16
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        memo = {}

        def dp(start: int):
            if start == len(s):
                return True
            if start in memo:
                return memo[start]
            
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in wordDict and dp(end):
                    memo[start] = True
                    return True
            
            memo[start] = False
            return False

        return dp(0)


        # def construct(current,wordDict, memo={}):
        #     if current in memo:
        #         return memo[current]

        #     if not current:
        #         return True

        #     for word in wordDict:
        #         if current.startswith(word):
        #             new_current = current[len(word):]
        #             if construct(new_current,wordDict,memo):
        #                 memo[current] = True
        #                 return True

        #     memo[current] = False
        #     return False

        # return construct(s,wordDict)