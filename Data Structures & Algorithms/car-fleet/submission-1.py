class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = sorted(zip(position, speed), reverse=True)
        sorted_position, sorted_speed = zip(*combined)
        position = list(sorted_position) 
        speed = list(sorted_speed)
        time = [(target-position[index])/speed[index] for index in range(len(position))]

        stack = []
        for current_time in time:
            if stack and stack[-1] >= current_time:
                continue 
            else:
                stack.append(current_time)
        
        return len(stack)
            
