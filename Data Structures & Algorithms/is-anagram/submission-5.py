class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
        
        s_set = set()
        t_set = set()

        for index in range(len(s)):
            if s[index] not in s_set:
                s_set.add(s[index])
            if t[index] not in t_set:
                t_set.add(t[index])

        
        return s_set == t_set

        