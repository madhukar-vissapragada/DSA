class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        result = None

        while low <= high:
            mid = (low + high) // 2 
            if Solution.helper(nums, k, mid):
                high = mid - 1 
                result = mid 
            else:
                low = mid + 1  
            
        return result

    @staticmethod
    def helper(nums: List[int], k: int, mid: int) -> bool:
        current_sum = 0 
        count = 1

        for current in nums:
            if current_sum + current > mid:
                current_sum = current 
                count += 1 
            else:
                 current_sum += current 
        
        return count <= k

        

        