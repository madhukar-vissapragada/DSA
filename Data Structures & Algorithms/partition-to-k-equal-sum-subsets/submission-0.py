class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        result = []
        self.solve(nums, 0, [], result)
        map = {}
        for current in result:
            key = sum(current) 
            if key in map:
                map[key].append(current)
            else:
                map[key] = [current]

        for key, value in map.items():
            if len(map[key]) == k:
                return True

        return False 
    

    def solve(self, nums: List[int], current_index: int, current_subset: List[int], result: List[List[int]]):
        if current_index == len(nums):
            result.append(current_subset.copy())
            return 
        
        current_subset.append(nums[current_index])
        self.solve(nums, current_index + 1, current_subset, result)
        current_subset.pop()
        self.solve(nums, current_index + 1, current_subset, result)
        