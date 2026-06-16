class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        self.solve(candidates, target, 0, [], result)
        return result 

    
    def solve(self, nums: List[int], target: int, current_index: int, 
                    current_combination: List[int], result: List[List[int]]):
            if target == 0:
                result.append(current_combination.copy())
                return
             
            for index in range(current_index, len(nums)):
                if index > current_index and nums[index] == nums[index - 1]:
                    continue 
                if target >= nums[index]:
                    current_combination.append(nums[index])
                    self.solve(nums, target-nums[index], index + 1, current_combination, result)
                    current_combination.pop()