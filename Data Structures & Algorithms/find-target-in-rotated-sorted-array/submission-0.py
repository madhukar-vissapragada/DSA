class Solution:
    def search(self, A: List[int], target: int) -> int:
        low = 0 
        high = len(A) - 1 

        while low <= high:
            mid = (low + high) // 2 

            if A[mid] == target:
                return mid 
            
            if A[low] < A[mid]:
                if A[mid] < target  and A[low] >= target:
                    high = mid - 1 
                else:
                    low = mid + 1 
            else:
                if A[mid] > target and A[high] <= target:
                    low = mid + 1 
                else:
                    high = mid - 1 
        
        return -1 
        