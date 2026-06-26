class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        self.solve(s, wordDict, 0, [], result)
        return result 

    def solve(self, s: str, word_dict: set, current_index: int, current_configuration: List[str], result: List[str]):
        if current_index == len(s):
            result.append(' '.join(current_configuration.copy()))
            return 
        
        for index in range(current_index, len(s)):
            left_part = s[current_index:index + 1]
            if left_part in word_dict:
                current_configuration.append(left_part)
                self.solve(s, word_dict, index + 1, current_configuration, result)
                current_configuration.pop()
        


        