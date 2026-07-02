class Solution:
    def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0 
        j = 0 

        while j < len(arr):
            if arr[j] == 0:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1 

            j += 1  

        