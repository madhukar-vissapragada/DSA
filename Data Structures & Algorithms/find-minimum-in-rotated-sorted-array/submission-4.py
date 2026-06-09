class Solution:
    def findMin(self, A: List[int]) -> int:
        low = 0
        high = len(A) - 1

        ans = 1001


        while low <= high:
            mid = (low + high) // 2
            if (mid > 0 and A[mid] < A[mid - 1]) and (mid < len(A) - 1 and (A[mid] < A[mid + 1])):
                return A[mid]

            if A[low] < A[mid]:
                ans = min(ans, A[low])
                low = mid + 1
            else:
                ans = min(ans, A[high])
                high = mid - 1

        return ans
