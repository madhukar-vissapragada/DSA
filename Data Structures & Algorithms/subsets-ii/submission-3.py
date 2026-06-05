class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.solve(nums, 0, [], result)
        return result  
    
    def solve(self, nums: List[int], current_index: int, current_subset: List[int], result: set):
        result.append(current_subset[:])

        for index in range(current_index, len(nums)):
            if index > current_index and nums[index] == nums[index - 1]:
                continue 
            
            current_subset.append(nums[index])
            self.solve(nums, index + 1, current_subset, result)
            current_subset.pop()
