class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False 
    
        stack = []
        for current in s:
            if current == ')' and len(stack) and stack[-1] == '(':
                stack.pop()
            elif current == ']' and len(stack) and stack[-1] == '[':
                stack.pop()
            elif current == '}' and len(stack) and stack[-1] == '{':
                stack.pop()
            else:
                stack.append(current)
        
        return len(stack) == 0
            
        