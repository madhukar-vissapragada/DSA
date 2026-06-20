class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        result = None 

        for index, value in enumerate(nums):
            res = target - value 

            if res in hash_map:
                result = [hash_map[res], index]
                break 
            else:
                hash_map[value] = index

        return result         