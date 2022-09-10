# Ref

* [手把手刷array - 雙指針秒殺7道 array 題目](https://labuladong.github.io/algo/2/20/23/)

# 雙指針

* 雙指針技巧經常用於 - array, linked-list，主要分為 `左右指針`, `快慢指針`
* 左右指針 - 兩個指針相向而行 / 相背而行
* 快慢指針 - 同向而行 - 一快一慢
* linked list 中的技術大概都屬於快慢指針，[ref](https://labuladong.github.io/algo/2/19/18/)，多半使用 fast, slow 兩個指針來操作
  * 判斷鍊錶有沒有環
  * 倒數第K個節點
* array 沒有實質意義的指針，可以把 index 當作指針

# 快慢指針


* **常見的應用希望你原地修改array內容**


## Leetcode 26, 刪除已排序數組中的重複元素
  * replace in place - 題目要求，不能多 new 一個 array
* sol 1 :
  * 重複的元素必定連在一起，每次找到重複就刪除，array 中的元素刪除，涉及到資料搬移(copy, paste)
  * sc O(1) , tc : O(N^2)，[ref](https://wiki.python.org/moin/TimeComplexity)
* sol 2 : how about 開一個新的 list，找到重複值不做事，找到不重複值就加入到新的 array?
  * sc : O(N), tc O(N)
* sol 3 : 
  * 透過快慢指針 - slow 走後面，fast 走前面，美找到一個不重複嚴肅，slow += 1 --> `nums[0 .. slow]` 都會是無重複元素，當 `fast` 走完之後，`nums[0 .. slow]` 就會是去重複的結果
  * <img src='../../assets/003array_1.gif'></img>
  * sc : O(1), tc : O(N)

```python

def removeDuplicates (nums : List[int]) -> List[int]:
    '''
    return 不重複的 array
    '''
    if len(nums) == 0:
        return []
    slow = 0
    fast = 0
    while fast < len(nums):
        if nums[fast] != nums[slow]:
            # 找到獨立值，將獨立值放置array中，將 duplciates 替換掉
            slow += 1
            nums[slow] = nums[fast] 
        fast += 1
    return nums[0:slow]

```

## Leetcode 83, 刪除已排序LinkedList中的重複元素 

https://leetcode.com/problems/remove-duplicates-from-sorted-list/submissions/

以上思維也適用於 leetcode 83，刪除已排序 linked list 中的重複元素，唯一的差異只是把 array 給值變成指針操作

<img src='../../assets/003array_2.gif'></img>

* 根據語言不同，需要考慮是否要進行 garbage collection， C++ 就需要，python 就不用


## Leetcode 27 - 原地刪除指定元素

https://leetcode.com/problems/remove-element/

* 除了去重複(原地修改)，也可能會碰到原地刪除
* `nums = [0,1,2,2,3,0,4,2], val = 2`
* out = 5, first at index = 2, final at index at 7, k = 7-5 = 2
* do not allocate extra space for another array
* Sol 1 :
  * 單指標 i, 記錄值 first_match_idx, current_match_idx，掃一遍 array
  * tc O(N), sc O(1)
  * 但這個做法沒辦法做到刪除元素
* Sol 2 :
  * 雙指標, fast, slow, 遇到 val 就跳過，剩下的都給 slow
  * 其實要 inplace 刪除，基本上都不是 remove，而是 slicing

```python
slow = 0
fast = 0
iteration 0, slow = 0, fast = 0

num[fast] != 2
num[slow] = nums[fast] # [0]

iteration 1, slow = 1, fast = 1
num[fast] != 2
num[slow] = nums[fast] # [0, 1]

iteration 2, slow = 2, fast = 2

num[fast] == 2

iteration 3, slow = 2, fast = 3

num[fast] == 2

iteration 4, slow = 2, fast = 4

num[fast] != 2

num[slow] = nums[fast] # [0, 1, 3]

...

final num[:slow] = [0,1,3,0,4]

```

## Leetcode 283 - 移動0

```
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
```

* 並沒有要求不能創造新的 array

* sol 1:
  * 把所有的 0 都移到最後面
  * 其實就是刪除0的意思(並非實質意義上的刪除，而是 slicing)，而慢指針後面都放 0
  * tc O(N)
  * sc O(1)
* sol 2:
  * 開一個 array，一個 counter
  * 是 0， counter +=1
  * 非 0， 加入 array
  * tc O(N)
  * sc O(N)

# 滑動窗口

* array 另一大類使用快慢指針的題目是 滑動窗口，而這是另一個主題

# 左右指針

* binary search