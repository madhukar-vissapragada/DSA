class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.ans = 0 
        self.solve(nums, 0, 0)
        return self.ans  
    

    def solve(self, nums: List[int], current_index: int, current_xor: int):
        if current_index == len(nums):
            self.ans += current_xor
            return 
        
        self.solve(nums, current_index + 1, current_xor ^ nums[current_index])
        self.solve(nums, current_index + 1, current_xor)
            