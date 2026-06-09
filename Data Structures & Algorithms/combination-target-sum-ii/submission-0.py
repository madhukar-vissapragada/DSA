class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = set()
        candidates.sort()
        self.solve(candidates, target, 0, [], result)

        return [list(x) for x in result]
    

    def solve(self, nums, target, current_index, current_subset, result):
        if target == 0:
            result.add(tuple(current_subset.copy()))
            return 

        if current_index == len(nums):
            return 

        if target >= nums[current_index]:
            current_subset.append(nums[current_index])

            self.solve(
                nums,
                target - nums[current_index],
                current_index + 1,
                current_subset,
                result
            )

            current_subset.pop()
        
        self.solve(nums, target, current_index + 1, current_subset, result)