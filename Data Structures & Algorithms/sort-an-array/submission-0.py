class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.merge_sort(nums, 0, len(nums)-1) 

    def merge_sort(self, nums: List[int], start: int, end: int):
        if start < end:
            mid = (start + end) // 2 
            self.merge_sort(nums, start, mid)
            self.merge_sort(nums, mid + 1, end)
            self.merge(nums, start, mid, end)
        return nums 
    
    def merge(self, nums: List[int], start: int, mid: int, end: int):
        left_size  = mid - start + 1 
        right_size = end - mid 

        left_array = []
        right_array = []

        temp_start = start
        for index in range(left_size):
            left_array.append(nums[temp_start])
            temp_start += 1 
        
        temp_start = mid + 1
        for index in range(right_size):
            right_array.append(nums[temp_start])
            temp_start += 1 
        
        i = j = 0 
        while i < len(left_array) and j < len(right_array):
            if left_array[i] <= right_array[j]:
                nums[start] = left_array[i]
                i += 1 
            else:
                nums[start] = right_array[j]
                j += 1 
            
            start += 1 
        
        while i < len(left_array):
            nums[start] = left_array[i]
            i += 1 
            start += 1 
        
        while j < len(right_array):
            nums[start] = right_array[j]
            j += 1 
            start += 1 

    
        






        