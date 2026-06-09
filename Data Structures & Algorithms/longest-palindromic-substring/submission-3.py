class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.solve(s)

    def solve(self, s: str) -> str:
        if len(s) == 1:
            return s 
        if len(s) == 2:
            if s[0] == s[1]:
                return s 
            return s[0]
        max_length = 1
        result = s[0]
        for current_index in range(len(s)):
            left = right = current_index
            if len(s) % 2 == 0:
                left = current_index
                right = current_index + 1

            while left >= 0 and right < len(s):
                if s[left] != s[right]:
                    break

                left -= 1
                right += 1

            current_length = right - left + 1 
            if current_length > max_length:
                result = s[left + 1: right]
                max_length = current_length

        return result