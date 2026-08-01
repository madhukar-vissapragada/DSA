class Solution:
    def dailyTemperatures(self, arr: List[int]) -> List[int]:
        stack = []
        result = []

        for index in range(len(arr)-1, -1, -1):
            while stack and arr[stack[-1]] <= arr[index]:
                stack.pop()
            
            result.append(stack[-1]-index if stack else 0)
            stack.append(index)
        
        return result[::-1]