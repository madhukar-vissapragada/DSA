class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for current in asteroids:
            if current > 0:
                stack.append(current)
            else:
                while stack and stack[-1] < abs(current):
                    stack.pop()
                
                
                if not stack:
                    stack.append(current)
                
                if stack[-1] == abs(current):
                    stack.pop()
        
        return stack 