class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(nums, target, 0, [], result)
        return result  
    
    def solve(self, nums: List[int], target: int, current_index: int, 
                    current_combination: List[int], result: List[List[int]]):
            if target == 0:
                result.append(current_combination.copy())
                return
             
            for index in range(current_index, len(nums)):
                if target >= nums[index]:
                    current_combination.append(nums[index])
                    self.solve(nums, target-nums[index], index, current_combination, result)
                    current_combination.pop()
            
        