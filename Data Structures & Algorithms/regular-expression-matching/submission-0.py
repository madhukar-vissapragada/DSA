class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.solve(s, p, 0, 0, {})

    def solve(self, s: str, p: str, i: int, j: int, memo: dict) -> bool:
        if i == len(s) and j == len(p):
            return True
        if i >= len(s) and j < len(p):
            return False

        if j == len(p):
            return True
        

        current_key = (i, j)
        if current_key in memo:
            return memo[current_key]

        consider = not_consider = False
        if j + 1 < len(p) and p[j + 1] == '*':
            consider = self.solve(s, p, i + 1, j, memo)
            not_consider = self.solve(s, p, i, j + 2, memo)
        equal = False
        if s[i] == p[j] or p[j] == '.':
            equal = self.solve(s, p, i + 1, j + 1, memo)

        result = equal or (consider or not_consider)
        memo[current_key] = result
        return result