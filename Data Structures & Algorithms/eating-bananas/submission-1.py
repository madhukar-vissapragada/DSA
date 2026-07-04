class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        result = None

        while low <= high:
            mid = (low + high) // 2

            if Solution.helper(piles, mid, h):
                result = mid 
                high = mid - 1 
            else:
                low = mid + 1 
        
        return result 

    @staticmethod
    def helper(piles:List[int], mid: int, h: int):
        total_hours = 0
        for current in piles:
                total_hours += math.ceil(current / mid)
        
        return total_hours <= h
