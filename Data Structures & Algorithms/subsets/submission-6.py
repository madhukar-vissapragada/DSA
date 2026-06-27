class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.solve(nums, 0, [], result)
        return result  
    
    def solve(self, nums: List[int], current_index: int, current_config: List[int], result: List[List[int]]):
        if current_index == len(nums):
            result.append(current_config.copy())
            return 
        
        # choose 
        current_config.append(nums[current_index])
        self.solve(nums, current_index + 1, current_config, result)
        current_config.pop()
        # not choose
        self.solve(nums, current_index + 1, current_config, result)
    
        