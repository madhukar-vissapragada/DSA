class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        map = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        
        def solve(column_number):
            if column_number < 10:
                return map[column_number] 
            
            return solve(column_number // 26) + map[column_number % 26]

        return solve(columnNumber)
        