

# https://leetcode.com/problems/n-queens/description/

from typing import List


class BK:
   def __init__(self):
      self.res = []
      self.verbose = False


   # 主函数，输入一组不重复的数字，返回它们的全排列
   def sove_n_queens(self, n : int) -> List[List[str]]:
      # nums = [1,2,3]
      # create a 2D board based on n
      board = [
         ["."] * n
         for _ in range(n)
      ]
      # [
      #  [....],
      #  [....], 
      #  [....],
      #  [....], 
      # ]
      if self.verbose:
         print(board)
      self.backtrack(board, 0)
      return self.res
   
   def backtrack(self, board : List[List[str]], row : int) -> None:
      # end with get all tracks(path)
      if self.verbose:
         print(f'res : {self.res}, track : {board}, row : {row}')
      
      if row == len(board):
         # 找到合法解，將整個 2D 棋盤加入 res
         self.res.append([
            "".join(row) 
            for row in board
            ])
         return None
      
      n_cols = len(board[row])
      # 4
     
      for col in range(n_cols):
         # 0,1,2,3
         # 排除不合法的選擇，剪枝
         if not self.is_valid(board, row, col):
            # nums[i] 已經在 track 中, skip
            continue
         
         #做選擇
         board[row][col] = "Q"
         # # 進入下一層決策樹
         self.backtrack(board, row+1)
         # # 撤銷選擇
         board[row][col] = '.'
         # used[i] = False

   def is_valid(self, board : List[List[str]], row : int, col : int) -> bool:
      '''
      tc : O(3N) ~ O(N)
      '''
      # Fix col, to check valid or not
      n_rows = len(board) # 4
      n_cols = n_rows # it's a square
      for r in range(n_rows):
         if board[r][col] == 'Q':
            # 直 & 橫都不能有
            return False
      
      # 只要檢查，左上，右上，因為左下、右下沒放皇后，不用檢查
      # 右上
      x, y = row - 1, col + 1
      while x >= 0 and y < n_cols:
         if board[x][y] == 'Q':
            return False
         # 持續往右上移動
         x -= 1
         y += 1
      
      # 左上
      x, y = row - 1, col - 1
      while x >= 0 and y >= 0:
         if board[x][y] == 'Q':
            return False
         
         # 持續往左上移動
         x -= 1
         y -= 1
         
      return True



questions = [
    (1, [['Q']]),
    (2,[]),
    (3,[]),
    (4,[
   [".Q..",
   "...Q",
   "Q...",
   "..Q."],
   ["..Q.",
   "Q...",
   "...Q",
   ".Q.."]
   ])
]

for q in questions:
   n, sol = q
   pred = BK().sove_n_queens(n)
   assert pred == sol
   print(BK().sove_n_queens(n))
   
