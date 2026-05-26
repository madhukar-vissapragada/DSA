class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self.solve(candidates, target, 0, [], result)
        return result 
    

    def solve(self, candidates: List[int], target: int, current_index: int, current_combination: List[int], result: List[List[int]]):
        if target == 0:
            result.append(current_combination.copy())
            return 
        
        if current_index == len(candidates):
            return 
        
        if target >= candidates[current_index]:
            current_combination.append(candidates[current_index])
            self.solve(candidates, target-candidates[current_index], current_index, current_combination, result)
            current_combination.pop()
        
        self.solve(candidates, target, current_index + 1, current_combination, result)
