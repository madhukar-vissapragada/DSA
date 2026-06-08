class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        self.solve(nums, 0, [], result)
        return list(result)

    def solve(
        self,
        nums: List[int],
        current_index: int,
        current_combination: List[int],
        result: set
    ):
        if current_index == len(nums):
            result.add(tuple(current_combination.copy()))
            return

        current_combination.append(nums[current_index])
        self.solve(nums, current_index + 1, current_combination, result)
        current_combination.pop()
        self.solve(nums, current_index + 1, current_combination, result)
