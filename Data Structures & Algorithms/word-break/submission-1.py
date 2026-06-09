class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self.solve(s, 0, set(wordDict)) 
    

    def solve(self, s: str, start: int, word_dict: set) -> bool:
        if start == len(s):
            return True 
        

        result = s[start] in word_dict
        for index in range(start + 1, len(s)):
            if s[start: index+1] in word_dict:
                result = True
                result = result and self.solve(s, index+1, word_dict)
        
        return result 
        