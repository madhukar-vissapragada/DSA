class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        return self.solve(nums, 0) 
    

    def solve(self, nums: List[int], start: int) -> int:
        if start == len(nums):
            return 0
        
        max_result = float('inf')
        current_result = 1
        for index in range(start, len(nums)):
            current_result *= nums[index]
        
        return max(current_result, self.solve(nums, start + 1))

        

            
        