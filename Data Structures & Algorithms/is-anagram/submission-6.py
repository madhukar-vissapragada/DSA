class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = {}
        t_map = {}

        for index in range(len(s)):
            if s[index] in s_map:
                s_map[s[index]] += 1 
            else:
                s_map[s[index]] = 1 
            
            if t[index] in t_map:
                t_map[t[index]] += 1 
            else:
                t_map[t[index]] = 1 
        
        return s_map == t_map


        