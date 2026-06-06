class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        self.solve(nums, 0, result)
        return list(result)
    
    def solve(self, nums: List[int], current_index: int, result: List[List[int]]):
        if current_index == len(nums):
            result.add(tuple(nums[:]))
            return 
        

        for index in range(current_index, len(nums)):
            nums[index], nums[current_index] = nums[current_index], nums[index]
            self.solve(nums, current_index + 1, result)
            nums[index], nums[current_index] = nums[current_index], nums[index]
        
