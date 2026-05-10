class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_h = {} 
        t_h = {}

        for current in s:
            if current in s_h:
                s_h[current] += 1 
            else:
                s_h[current] = 1
        
        for current in t:
            if current in t_h:
                t_h[current] += 1 
            else:
                t_h[current] = 1 
        
        if len(s_h) != len(t_h):
            return False 
        
        for key, value in s_h.items():
            if key not in t_h:
                return False 

            if t_h[key] != value:
                return False 

        return True 
        


        