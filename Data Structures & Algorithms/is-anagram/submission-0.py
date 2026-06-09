class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_set = set()

        for current in s:
            hash_set.add(current) 
        
        for current in t:
            if current not in hash_set:
                return False 
        
        return True
        