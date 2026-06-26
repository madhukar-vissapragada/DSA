class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        grid = [['.'] * n for _ in range(n)]
        self.solve(n, 0, grid, result)
        return result 
    
    def solve(self, n: int, current_row: int, grid: List[List[str]], result: List[str]):
        if current_row == n:
            result.append([''.join(row) for row in grid])
            return 
        

        for current_col in range(n):
            if Solution.is_valid(grid, current_row, current_col, n):
                grid[current_row][current_col] = 'Q'
                self.solve(n, current_row + 1, grid, result)
                grid[current_row][current_col] = '.'
    
    @staticmethod
    def is_valid(grid, row, col, n):
        def is_row_valid(grid, row, n):
            for col in range(n):
                if grid[row][col] == 'Q':
                    return False 
            
            return True 
        
        def is_col_valid(grid, col, n):
            for row in range(n):
                if grid[row][col] == 'Q':
                    return False 
            
            return True 
        
        def is_diagonally_valid(gird, row, col, n):
            # left top 
            current_row = row 
            current_col = col

            while current_row >= 0 and current_col >= 0:
                if grid[current_row][current_col] == 'Q':
                    return False 
                
                current_row -= 1 
                current_col -= 1 
            
            # right top 
            current_row = row 
            current_col = col

            while current_row >= 0 and current_col < n:
                if grid[current_row][current_col] == 'Q':
                    return False 
                
                current_row -= 1 
                current_col += 1 
            
            return True 
        
        return (is_row_valid(grid, row, n) and is_col_valid(grid, col, n) 
                and is_diagonally_valid(grid, row, col, n))
        
        
            
