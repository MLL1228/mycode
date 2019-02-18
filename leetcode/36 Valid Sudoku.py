class Solution:
    def isValidSudoku(self, board: 'List[List[str]]') -> 'bool':
        row_set=[]
        col_set=[]
        arr_set=[]

        for row in range(9):
            for col in range(9):
                if col == 0:
                    row_set.append(set())
                if row == 0:
                    col_set.append(set())
                if row % 3 == 0 and col % 3 == 0:
                    arr_set.append(set())

                if board[row][col].isdigit():
                    if board[row][col] in row_set[row]:
                        # print('1. row', row, "  col", col)
                        return False
                    else:
                        row_set[row].add(board[row][col])

                    if board[row][col] in col_set[col]:
                        # print('2. row', row, "  col", col)
                        return False
                    else:
                        col_set[col].add(board[row][col])

                    arr_index = (row - row % 3) + col // 3
                    if board[row][col] in arr_set[arr_index]:
                        # print(arr_index)
                        # print('3. row', row, "  col", col)
                        return False
                    else:
                        arr_set[arr_index].add(board[row][col])

        return True




mylist = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

s = Solution()
res = s.isValidSudoku(mylist)
print(res)










