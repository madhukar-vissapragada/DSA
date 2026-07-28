class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for current in operations:
            if current == '+':
                stack.append(stack[-1] + stack[-2])
            elif current == 'D':
                stack.append(stack[-1] * 2)
            elif current == 'C':
                stack.pop()
            else:
                stack.append(int(current))
        
        return sum(stack)
        