class Solution:
    def climbStairs(self, n: int) -> int:
        return self.solve(0, n) 
    
    def solve(self, current_stair:int, n:int) -> int:
        if current_stair == n:
            return 1
        
        if current_stair > n:
            return 0

        one_step = self.solve(current_stair + 1, n)
        two_step = self.solve(current_stair + 2, n)

        return one_step + two_step
