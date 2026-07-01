class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            filtered_row = [item for item in row if item != "."]
            row_set = set(filtered_row)
            if len(row_set) != len(filtered_row):
                return False

        for i in range(len(board)):
            col = [row[i] for row in board]
            filtered_col = [item for item in col if item != "."]
            col_set = set(filtered_col)
            if len(col_set) != len(filtered_col):
                return False
        
        for i in range(len(board)):
            row_num = i / 3
            col_num = i % 3
            cols = [board[j] for j in range(len(board)) if j >= row_num * 3 and j < row_num * 3 + 3]
            square = []

            for k in range(len(cols)):
                square += [cols[k][j] for j in range(len(cols[k])) if j >= col_num * 3 and j < col_num * 3 + 3]

            filtered_square = [item for item in square if item != "."]
            square_set = set(filtered_square)
            if len(square_set) != len(filtered_square):
                return False
        
        return True
