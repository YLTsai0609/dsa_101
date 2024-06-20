

from typing import Optional, List


class BK:
   def __init__(self):
      self.res = []
      self.verbose = True


   # 主函数，输入一组不重复的数字，返回它们的全排列
   def permute(self, nums: List[int]) -> List[List[int]]:
      # nums = [1,2,3]
      # 记录「路径」
      track = []
      # 「路径」中的元素会被标记为 true，避免重复使用
      used = [False] * len(nums)
      # used = [False, False, False]
      
      self.backtrack(nums, track, used)
      return self.res
   def backtrack(self, nums : List[int], track : List[int], used:List[bool]) -> None:
      # end with get all tracks(path)
      if self.verbose:
         print(f'res : {self.res}, track : {track}, used : {used}')
      if len(track) == len(nums):
         self.res.append(track.copy())
         return 
      for i in range(len(nums)):
         # 排除不合法的選擇，剪枝
         if used[i]:
            # nums[i] 已經在 track 中, skip
            continue
         
         #做選擇
         track.append(nums[i])
         used[i] = True
         # 進入下一層決策樹
         self.backtrack(nums, track, used)
         # 撤銷選擇
         track.pop()
         used[i] = False


questions = [
    ([1,2,3], [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]),
    ([0,1],[[0,1],[1,0]]),
    ([1], [[1]])
]

for q in questions:
   nums, sol = q
   pred = BK().permute(nums)
   assert pred == sol
   print(nums, BK().permute(nums))
