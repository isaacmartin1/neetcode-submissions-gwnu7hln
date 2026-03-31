class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        column = set()
        grid = set()

        # evaluate each row
        for row_i in range(len(board[0])):
            row = set()
            for column_i in range(len(board)):
                current_val = board[row_i][column_i]
                if current_val == '.':
                    continue
                if current_val in row:
                    return False
                row.add(current_val)
        
        # evaluate each column
        for column_i in range(len(board)):
            column = set()
            for row_i in range(len(board[0])):
                current_val = board[row_i][column_i]
                if current_val == '.':
                    continue
                if current_val in column:
                    return False
                column.add(current_val)
        
        # evaluate each 3x3 square
        y_adjuster = 0
        x_adjuster = 0
        
        for x_adjuster in [0,3,6]:
            for y_adjuster in [0,3,6]:
                square_set = set()
                for x_idx in range(3):
                    for y_idx in range(3):
                        current_val = board[x_idx + x_adjuster][y_idx + y_adjuster]
                        if current_val == '.':
                            continue
                        if current_val in square_set:
                            return False
                        square_set.add(current_val)



        return True
        