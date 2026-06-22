class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_map = {}
        result = None

        for current in nums:
            hash_map[current] = hash_map.get(current, 0) + 1
        
        for key, value in hash_map.items():
            if value > (len(nums) // 2):
                result = key 
                break 
        
        return result 
        