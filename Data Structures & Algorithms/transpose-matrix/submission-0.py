class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        result = []
        rows = len(matrix)
        cols = len(matrix[0])

        for col in range(cols):
            current_row = []
            for row in range(rows):
                current_row.append(matrix[row][col])
            
            result.append(current_row)

        return result