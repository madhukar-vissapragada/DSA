class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.solve(s, set(wordDict), 0)
    

    def solve(self, s: str, word_dict: set, start: int) -> bool:
        if start == len(s):
            return True 
        
        for index in range(start, len(s)):
            if s[start:index+1] in word_dict:
                if self.solve(s, word_dict, index + 1):
                    return True 

        return False 
                



