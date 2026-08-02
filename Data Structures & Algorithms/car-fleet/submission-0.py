class Solution:
    import math
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        hash_map = {}
        for index in range(len(position)):
            to_cover = target - position[index]
            time = math.ceil(to_cover / speed[index])
            if time in hash_map:
                hash_map[time].append(position[index])
            else:
                hash_map[time] = [position[index]]
        
        return len(hash_map)