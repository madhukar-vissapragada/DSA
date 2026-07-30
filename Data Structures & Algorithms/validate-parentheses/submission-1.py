class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for current in s:
            if current == ')' and stack and stack[-1] == '(':
                stack.pop()
            elif current == ']' and stack and stack[-1] == '[':
                stack.pop()
            elif current == '}' and stack and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(current)
        
        return len(stack) == 0
        