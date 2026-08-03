from typing import *

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        prev_s = self.prev_small(heights)
        next_d = self.next_small(heights)
        largest = 0
        for index in range(len(heights)):
            width = next_d[index] - prev_s[index] - 1
            area = heights[index] * width
            largest = max(largest, area)
        return largest

    def prev_small(self, heights: List[int]):
        result = []
        stack = []

        for index in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[index]:
                stack.pop()
            result.append(-1 if not stack else stack[-1])
            stack.append(index)
        return result

    def next_small(self, heights: List[int]):
        result = []
        stack = []

        for index in range(len(heights) - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[index]:
                stack.pop()

            result.append(len(heights) if not stack else stack[-1])
            stack.append(index)
        return result[::-1]