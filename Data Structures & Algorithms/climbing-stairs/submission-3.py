class Solution:
    def climbStairs(self, n: int) -> int:
        return self.solve(0, n)
    
    def solve(self, current_stair: int, n: int):
        if current_stair == n:
            return 1 
        if current_stair > n:
            return 0 
        
        return self.solve(current_stair + 1, n) + self.solve(current_stair + 2, n)
        