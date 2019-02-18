# class Solution:
#     def solveSudoku(self, board: 'List[List[str]]') -> 'None':
#         """
#         Do not return anything, modify board in-place instead.
#         """
#
#         select = '.'
#         row_set = []
#         col_set = []
#         arr_set = []
#
#         for row in range(9):
#             for col in range(9):
#                 if col == 0:
#                     row_set.append(set('123456789'))
#                 if row == 0:
#                     col_set.append(set('123456789'))
#                 if row % 3 == 0 and col % 3 == 0:
#                     arr_set.append(set('123456789'))
#
#                 if board[row][col].isdigit():
#                     row_set[row].remove(board[row][col])
#                     col_set[col].remove(board[row][col])
#                     arr_index = (row - row % 3) + col // 3
#                     arr_set[arr_index].remove(board[row][col])
#
#
#         flag = True
#
#         while flag:
#             row1 = 0
#             col1 = 0
#             while row1 < 9:
#
#                 if board[row1][col1] == select:
#                     arr_index1 = (row1 - row1 % 3) + col1 // 3
#                     inter_set = row_set[row1] & col_set[col1] & arr_set[arr_index1]
#                     count = 0
#                     for i in inter_set:
#                         count += 1
#                     if count == 1:
#                         for i in inter_set:
#                             board[row1][col1] = i
#                             row_set[row1].remove(i)
#                             col_set[col1].remove(i)
#                             arr_set[arr_index1].remove(i)
#                             col1 += 1
#                         break
#                 col1 += 1
#                 if col1 >= 9:
#                     row1 += 1
#                     col1 = 0
#             else:
#                 flag = False
#
#
#         print(board)
#         return

class Solution:
    def solveSudoku(self, board: 'List[List[str]]') -> 'None':
        """
        Do not return anything, modify board in-place instead.
        """

        select = '.'
        row_set = []
        col_set = []
        arr_set = []

        for row in range(9):
            for col in range(9):
                if col == 0:
                    row_set.append(set('123456789'))
                if row == 0:
                    col_set.append(set('123456789'))
                if row % 3 == 0 and col % 3 == 0:
                    arr_set.append(set('123456789'))

                if board[row][col].isdigit():
                    row_set[row].remove(board[row][col])
                    col_set[col].remove(board[row][col])
                    arr_index = (row - row % 3) + col // 3
                    arr_set[arr_index].remove(board[row][col])












mylist =[[".", ".", "9", "7", "4", "8", ".", ".", "."], ["7", ".", ".", ".", ".", ".", ".", ".", "."],
     [".", "2", ".", "1", ".", "9", ".", ".", "."], [".", ".", "7", ".", ".", ".", "2", "4", "."],
     [".", "6", "4", ".", "1", ".", "5", "9", "."], [".", "9", "8", ".", ".", ".", "3", ".", "."],
     [".", ".", ".", "8", ".", "3", ".", "2", "."], [".", ".", ".", ".", ".", ".", ".", ".", "6"],
     [".", ".", ".", "2", "7", "5", "9", ".", "."]]

s = Solution()
res = s.solveSudoku(mylist)
# print(res)















