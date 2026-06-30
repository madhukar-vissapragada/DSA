class Solution:
    def mySqrt(self, x: int) -> int:
        low = 0
        high = x 
        result = None

        while low <= high:
            mid = (low + high) // 2 

            if mid ** 2 <= x:
                result = mid 
                low = mid + 1 
            else:
                high = mid - 1
        
        return result
