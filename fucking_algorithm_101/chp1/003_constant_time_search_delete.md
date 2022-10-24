# Summary


1. 如果希望高效率地、等機率地隨機獲取元素，底層容器要選 Array
2. 如果希望 array 刪除的時間複雜度要 O(1)，那麼必須刪除的元素永遠在遠端，可以搭配一個 hash table 來實現這個機制
3. 如果希望隨機獲取元素，但有黑名單，可以在 hashtable 上做一些處理，避開黑名單元素

# Ref

* [常数时间删除-查找数组中的任意元素](https://labuladong.github.io/algo/2/20/33/)


* 如何結合 hash table 以及 array，使得 array 的 `刪除` 時間複雜度也變成 O(1)`

# 實作隨機集合 - leetcode 380

https://leetcode.com/problems/insert-delete-getrandom-o1/

* Insert, delete, get - 必須是 O(1)
* `getRandom` - 必須是同等機率 return elements

Analysis : 

hash table

* get : O(1)
* insert : O(1)
* get_random : O(1) 要取出，底層一定要是 array，而且 array 是緊密相鄰的(記憶體連續)
  * 生成隨機數字作為 index，並從 array 選出來 return 
* delete : 
  * 使用 array 來存， delete 沒辦法是 O(1)，會是 O(N)
  * **除非，該 element 永遠都在尾端**
    * 給定 `val`，先 swap 到 array 的尾端，再 pop
    * swap 用 hash table 來做

```python
import typing import Dict

class RandomizedSet:

  nums = []
  val2idx : Dict[int,int] = {}

  def insert(val : int) -> bool:
    # 檢查 val 在不在，在的話就不需插入
    if val in val2idx.keys():
      return False
    # 若 val 不存在，插入到 nums 的尾端
    val2idx[val] = len(nums)
    nums.appned(val)
    return True
  
  def remove(val : int) -> bool:
    # 如果 val 不存在，不需要刪橻
    if not val in val2idx.keys():
      return False
    
    # 執行刪除
    idx = val2idx[val]

    # 將要刪除的元素 swap 到 nums 的最後
    # 在進行 pop ， 能夠達成 O(1)
    swap(nums[idx], nums[-1])
    nums.pop()
    
    val2idx.pop(val)
    return True

  def get_random() -> int:
    return nums[rand() % len(nums)]

  def get(val):
    # O(1)
    pass
  
```

# 避開黑名單的隨機數 - leetcode 710

* 給定正整數 N，代表區間 `[0, N)`，並給定一個 blacklist，該資料結構需可以 return 隨機數，但不能在 blacklist 中


Sol 1 :
* 隨機取數，並檢查是否在 blacklist 中 --> blacklist
  * 需把 blacklist 也建立一個 hashtable, sc : O(B)
  * 執行效能和 rand 掛鈎

Sol 2 :
* pass



<!-- ```python
from typing import Dict

class RaodmizeWithBlackList:
  def __init__(self, n : int, blacklist : List[int]):
    self.nums = list(range(n))
    self.blacklist = blacklist
    self.val2idx = {
      val : idx
      for idx, val in enumerate(self.nums)
    }

    self.block_blacklist()

  def block_blacklist(self):
    for e in blacklist:
      self.validx.pop(e)

  def get_random() -> int:
    return nums[rand() % len(nums)]

``` -->

