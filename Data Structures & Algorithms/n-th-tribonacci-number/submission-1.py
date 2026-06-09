class Solution:
    def tribonacci(self, n: int) -> int:
        return self.solve(n, {}) 
    
    def solve(self, n:int, memo: dict) -> int:
        if n == 0:
            return 0 
        if n in (1, 2):
            return 1 
        
        return self.solve(n-1, memo) + self.solve(n-2, memo) + self.solve(n-3, memo)

        