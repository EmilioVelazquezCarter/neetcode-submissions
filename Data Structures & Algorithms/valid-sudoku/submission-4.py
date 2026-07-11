# [["1","2",".",".","3",".",".",".","."], 1
#  ["4",".",".","5",".",".",".",".","."], 2
#  [".","9","8",".",".",".",".",".","3"], 3
#  ["5",".",".",".","6",".",".",".","4"], 4
#  [".",".",".","8",".","3",".",".","5"], 5
#  ["7",".",".",".","2",".",".",".","6"], 6
#  [".",".",".",".",".",".","2",".","."], 7
#  [".",".",".","4","1","9",".",".","8"], 8
#  [".",".",".",".","8",".",".","7","9"]] 9
#    1   2   3   4   5   6   7   8   9          


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)
        
        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or
                    board[r][c] in cols[c] or 
                    board[r][c] in squares [(r //3, c //3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3, c//3)].add(board[r][c])
        return True
              