class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for index in range(len(nums)):
            found = False
            while nums[index] != index + 1:
                if nums[index] == nums[nums[index]-1]:
                    found = True 
                    break
                nums[index], nums[nums[index]-1] = nums[nums[index]-1], nums[index]
            
            if found:
                result = nums[index]
                break

        return result 
