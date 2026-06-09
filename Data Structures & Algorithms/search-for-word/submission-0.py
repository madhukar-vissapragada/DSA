class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        for i in range(rows):
            for j in range(cols):
                current_index = 0
                if word[current_index] == board[i][j]:
                    if self.solve(board, word, i, j, current_index, rows, cols):
                        return True 
        return False  
    

    def solve(self, board: List[List[str]], word: str, 
                    current_row: int, 
                    current_col: int, 
                    current_index: int, 
                    rows: int, cols: int):
        if current_index == len(word):
            return True 
        
        if current_row not in range(rows) or current_col not in range(cols):
            return False  
        
        if word[current_index] != board[current_row][current_col]:
            return False 
        
        right = self.solve(board, word, current_row, current_col + 1, current_index + 1, rows, cols)
        bottom = self.solve(board, word, current_row + 1, current_col, current_index + 1, rows, cols)

        return right or bottom 
        