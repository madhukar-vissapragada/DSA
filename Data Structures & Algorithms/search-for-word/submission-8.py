class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        for row in range(rows):
            for col in range(cols):
                if self.solve(board, word, 0, row, col, rows, cols):
                    return True 
        return False 
    
    def solve(self, board: List[List[str]], word: str, current_index: int, 
                    current_row: int, current_col: int, rows: int, cols: int):
        if current_index == len(word):
            return True

        if current_row not in range(rows) or current_col not in range(cols):
            return False 
        
        if board[current_row][current_col] != word[current_index]:
            return False 
        
        board[current_row][current_col] = -1 
        # up 
        up = self.solve(board, word, current_index + 1, current_row - 1, current_col, rows, cols)

        # left 
        left = self.solve(board, word, current_index + 1, current_row, current_col - 1, rows, cols)

        # right
        right = self.solve(board, word, current_index + 1, current_row, current_col + 1, rows, cols)

        # down 
        down = self.solve(board, word, current_index + 1, current_row + 1, current_col, rows, cols)

        board[current_row][current_col] = word[current_index]

        return up or left or right or down 
