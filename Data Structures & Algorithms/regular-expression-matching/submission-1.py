class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.solve(s, p, 0, 0)

    def solve(self, s: str, p: str, i: int, j: int) -> bool:
        if i == len(s) and j == len(p):
            return True

        if i < len(s) and j == len(p):
            return False
        
        if j + 1 < len(p) and p[j + 1] == '*':
            return (self.solve(s, p, i, j+2) or self.solve(s, p, i+1, j))
        
        if s[i] == p[j] or p[j] == '.':
            return self.solve(s, p, i + 1, j + 1)
        
        return False