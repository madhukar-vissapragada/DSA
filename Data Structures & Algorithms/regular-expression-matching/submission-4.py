class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.solve(s, p, 0, 0, {})

    def solve(self, s: str, p: str, i: int, j: int, memo: dict) -> bool:
        if j == len(p):
            return i == len(s)
        
        current_key = (i, j)
        first_match = i < len(s) and (s[i] == p[j] or p[j] == '.')

        if j + 1 < len(p) and p[j + 1] == '*':
            result =  (
                self.solve(s, p, i, j+2, memo) or self.solve(s, p, i+1, j, memo)
            )
            memo[current_key] = result 
            return result
        
        result = first_match and self.solve(s, p, i+1, j+1, memo)
        memo[current_key] = result
        return result
