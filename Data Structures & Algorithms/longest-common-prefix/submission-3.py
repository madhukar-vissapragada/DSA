class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        current_str = strs[0]

        for current in strs[1:]:
            i = 0 
            j = 0 

            result = ""
            while i < len(current_str) and j < len(current) and current_str[i] == current[j]:
                result += current_str[i]

                i += 1 
                j += 1 
            
            current_str = result 
        
        return current_str
