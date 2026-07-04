class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low = max(weights)
        high = sum(weights)
        result = None

        while low <= high:
            mid = (low + high) // 2
            if Solution.helper(weights, days, mid):
                result = mid
                high = mid - 1 
            else:
                low = mid + 1 
        
        return result 
            

    @staticmethod
    def helper(weights: List[int], days: int, mid: int) -> int:
        total_days = 1 
        current_weight = 0 

        for weight in weights:
            if current_weight + weight > mid:
                current_weight = weight 
                total_days += 1
            else:
                current_weight += weight     

        return total_days <= days
            

