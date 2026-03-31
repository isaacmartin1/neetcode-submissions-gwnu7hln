class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = collections.defaultdict(set)
        column = collections.defaultdict(set)
        grid = collections.defaultdict(set)

        # evaluate each row
        for row_i in range(len(board[0])):
            for column_i in range(len(board)):
                current_val = board[row_i][column_i]
                if current_val == '.':
                    continue
                
                if current_val in row[column_i]:
                    return False
                elif current_val in column[row_i]:
                    return False
                elif current_val in grid[column_i // 3, row_i // 3]:
                    return False

                row[column_i].add(current_val)
                column[row_i].add(current_val)
                grid[column_i // 3, row_i // 3].add(current_val)

        
        return True
        