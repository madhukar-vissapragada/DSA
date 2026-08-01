class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for current in asteroids:
            if current < 0:
                if stack[-1] == abs(current):
                    stack.pop()
            else:
                stack.append(current)
        return stack
        