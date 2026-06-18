class Solution:
    def climbStairs(self, n: int) -> int:
        return self.solve(0, n, {})
    
    def solve(self, current_stair: int, n: int, hash_map):
        if current_stair in hash_map:
            return hash_map[current_stair]
        if current_stair == n:
            return 1 
        if current_stair > n:
            return 0 
        
        
        
        result = self.solve(current_stair + 1, n, hash_map) + self.solve(current_stair + 2, n, hash_map)
        hash_map[current_stair] = result 
        return result 
        