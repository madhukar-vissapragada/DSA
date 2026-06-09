class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            if nums[index] != index + 1:
                corrected_index = nums[index] - 1 
                if nums[index] == nums[corrected_index]:
                    return nums[index]
            
                nums[index], nums[corrected_index] = nums[corrected_index], nums[index]
            else:
                index += 1 

