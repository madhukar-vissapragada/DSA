class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0 
        high = len(nums)-1
        min_element = 10 ** 9

        while low <= high:
            mid = (low + high)//2 

            min_element = min(nums[mid], min_element)

            if nums[mid] >= nums[low]:
                min_element = min(nums[low], min_element)
                low = mid + 1 
            else:
                high = mid - 1 
        
        return min_element

    

        