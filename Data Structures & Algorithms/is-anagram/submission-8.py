class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
                return False 
        hash_map = {}

        for current in s:
                if current in hash_map:
                        hash_map[current] += 1 
                else:
                        hash_map[current] = 1 
        
        for current in t:
                if current not in hash_map:
                        break 
                else:
                        hash_map[current] -= 1 
                        if hash_map[current] == 0:
                                del hash_map[current]

        return len(hash_map) == 0
        