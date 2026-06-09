class Solution:
    def rob(self, nums: List[int]) -> int:
        return self.solve(nums, 0) 
    
    def solve(self, nums: List[int], current_house: int) -> int:
        if current_house >= len(nums):
            return 0 
        
        rob = nums[current_house] + self.solve(nums, current_house + 2)
        do_not_rob = self.solve(nums, current_house + 1)

        result = max(rob, do_not_rob)
        return result 
    
        
        