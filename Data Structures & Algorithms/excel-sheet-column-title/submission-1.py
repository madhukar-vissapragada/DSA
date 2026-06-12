class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        map = ["", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        
        def solve(column_number: int) -> str:
            if column_number in range(1, 27):
                return map[column_number]
            
            remainder = column_number % 26 
            quotient  = column_number // 26 

            if remainder == 0:
                return solve(quotient - 1)
            
            return f"{solve(column_number // 26)}{map[remainder]}"
        
        return solve(columnNumber)