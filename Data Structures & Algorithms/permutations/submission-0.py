class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        map = [1 for _ in range(len(nums))]
        self.solve(nums, map, [], result)
        return result 
    
    def solve(self, nums: List[int], map: List[int], current_subset: List[int], result: List[int]):
        if len(current_subset) == len(nums):
            result.append(current_subset.copy())
            return 


        for index in range(len(nums)):
            if map[index]:
                map[index] = 0
                current_subset.append(nums[index])
                self.solve(nums, map, current_subset, result)
                map[index] = 1
                current_subset.pop()
        
                
