class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top_row = 0
        bot_row = len(matrix) - 1
        row_idx = -1

        while bot_row >= top_row and row_idx == -1:
            mid_row = (top_row + bot_row) // 2

            if matrix[mid_row][0] <= target:
                if mid_row == len(matrix) - 1 or (mid_row < len(matrix) - 1 and matrix[mid_row + 1][0] > target):
                    row_idx = mid_row
                    break
                top_row = mid_row + 1
            elif matrix[mid_row][0] > target:
                bot_row = mid_row - 1
        
        if row_idx == -1:
            return False
        
        left_col = 0
        right_col = len(matrix[0]) - 1

        while right_col >= left_col:
            mid_col = (left_col + right_col) // 2

            if matrix[row_idx][mid_col] < target:
                left_col = mid_col + 1
            elif matrix[row_idx][mid_col] > target:
                right_col = mid_col - 1
            else:
                return True

        return False