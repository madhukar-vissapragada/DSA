class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # perimeter of square = 4a, a = p//4
        area = 4 
        perimeter = sum(matchsticks)
        if perimeter % area == 0:
            required_area = perimeter // area
            return self.solve(0, matchsticks, [0] * len(matchsticks), area, required_area, required_area)

        return False 
    
    def solve(self, current_index: int, matchsticks: List[int], tracker:List[int],  area: int, target_area: int, req_area: int):
        if area == 0:
            return True 
        if target_area == 0:
            return self.solve(0, matchsticks, tracker, area-1, req_area, req_area)
        if current_index == len(matchsticks):
            return False 
        
        for index in range(current_index, len(matchsticks)):
            if tracker[index] == 0 and target_area >= matchsticks[index]:
                tracker[index] = 1 
                if self.solve(index + 1, matchsticks, tracker, area, target_area - matchsticks[index], req_area):
                    return True 
                tracker[index] = 0 
        
        return False 
    



        