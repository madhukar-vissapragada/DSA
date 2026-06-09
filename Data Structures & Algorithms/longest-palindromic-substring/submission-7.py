class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.solve(s, 0, len(s) - 1)

    def is_palindrome(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

    def solve(self, s: str, left: int, right: int) -> str:
        if left > right:
            return ""

        if self.is_palindrome(s, left, right):
            return s[left:right + 1]

        a = self.solve(s, left + 1, right)
        b = self.solve(s, left, right - 1)

        return a if len(a) > len(b) else b