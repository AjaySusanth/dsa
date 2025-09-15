# https://leetcode.com/problems/valid-sudoku/
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #Validate rows
        for i in range(9):
            s = set()
            for j in range(9):
                if board[i][j] in s:
                    return False
                elif board[i][j]!= ".":
                    s.add(board[i][j])
        
         #Validate cols
        for i in range(9):
            s = set()
            for j in range(9):
                if board[j][i] in s:
                    return False
                elif board[j][i]!= ".":
                    s.add(board[j][i])

        #Validate boxes

        start = [
            (0,0),(0,3),(0,6),
            (3,0),(3,3),(3,6),
            (6,0),(6,3),(6,6)       
        ]

        for row,col in start:
            s= set()
            for i in range(row,row+3):
                for j in range(col,col+3):
                    if board[i][j] in s:
                        return False
                    elif board[i][j]!= ".":
                        s.add(board[i][j])
        return True
        