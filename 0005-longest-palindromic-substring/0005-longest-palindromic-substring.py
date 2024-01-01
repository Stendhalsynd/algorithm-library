class Solution:
    def longestPalindrome(self, s: str) -> str:
        for i in range(len(s)):
            for start in range(i + 1):
                end = len(s) - i + start
                if s[start] == s[end - 1] and self.is_palindrome(s, start, end):
                    return s[start: end]

    def is_palindrome(self, s: str, start: int, end: int) -> bool:
        length = end - start
        for i in range(length // 2):
            if s[start + i] != s[end - 1 - i]:
                return False
        return True