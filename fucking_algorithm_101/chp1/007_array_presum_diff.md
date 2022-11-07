# Ref

* [小而美的算法技巧：前缀和数组](https://labuladong.github.io/algo/2/20/24/)
* [小而美的算法技巧：差分数组](https://labuladong.github.io/algo/2/20/25/)


# 1d array - presum leetcode 303

https://leetcode.com/problems/range-sum-query-immutable/

easy

* an integer array `nums`, implement `sumRange (left, right)` - with immutable array
  * `left <= right`

```
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]

Explanation
NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
numArray.sumRange(0, 2); // return (-2) + 0 + 3 = 1
numArray.sumRange(2, 5); // return 3 + (-5) + 2 + (-1) = -1
numArray.sumRange(0, 5); // return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3
```

```python
class NumArray:

    def __init__(self, nums: List[int]):
        

    def sumRange(self, left: int, right: int) -> int:
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
```

* 元素值在 -10^5 ~ 10^5
* Array 長度 1 ~ 10^4
* range(left, right), `0 <= left <= right < nums.length`
* sumRange 最多被 call 10^4 次


## Sol 1 Naive Loop

1. Naive Solution, query 數量 q, array大小 n, query(left, right)

```
class NumArray {

    private int[] nums;

    public NumArray(int[] nums) {
        this.nums = nums;
    }
    
    public int sumRange(int left, int right) {
        int res = 0;
        for (int i = left; i <= right; i++) {
            res += nums[i];
        }
        return res;
    }
}
```

* tc : O(q * (max-min)), worst case, min=0, max = n --> O(qn)

## Sol 2 - presum

* 先算好每個值，直接查表
* build presum table
  * sc : O(N)
  * tc : O(N)
* query for multiple query `q`
  * tc O(1)
* Compare sol 1 to sol 2
  * tc : O(qN) --> tc : O(q)
  * sc : O(1) --> sc : O(N)
* Compare to hash table solution
  * hash table 的 key 可以更有彈性， Array 只吃 index，但 hash table 也可以做
  * hash table sol 
    * `{ '0-1' :a, '0-2' : b, '0-3' : c}`
    * `range(1,2) = h['0-2']  - h['0-1']`
    * 時間複雜度、空間複雜度相同
    * 只是這題用 array 在 query 的時候更簡潔

```python
class NumArray:

  def __init__(self, nums: List[int]):
    # build presum array
    # nums=[2,5,1]
    n = len(nums)
    self.presum = [None for i in n + 1]
    presum[0] = 0

    for i in range(1, len(nums)):
      # gives [0, 2, 7, 8]
      presum[i] = presum[i-1] + nums[i - 1]

  def sumRange(self, left: int, right: int) -> int:
      # range(left, right) = presum[right] - presum[left]
      return presum[right + 1] - presum[left]

```

<img src='../../assets/7_1.png'></img>

* presum 多一個 0 不一定有必要，也可以簡化掉

# 查詢給定分數區間內的學生數量

* 場景 : 期中考，每個學生有一個分數
* 有多次查詢，每次查詢都是詢問 分數 range(a, b) 中有幾個學生

## presum

```python
scores = [] # 儲存所有學生的分數，e.g. [100, 30, 90]


# [0, 0, .... 1, ...., 1, 0, 1]
count = [0 for i in range(100 + 1)] # 記錄每個分數的學生有幾個
for s in scores:
  count[s] += 1


count_presum = [None for i in range(100 + 1)]
count_presum[0] = 0
for count_idx in range(1, len(count) + 1):
  count_presum[i] = count_presum[i-1] + count[i-1]

def query(count_presum ,left, right):
  return count_presum[right + 1] - count_presum[left]
```

# 2d-array presum leetcode 304

medium 

https://leetcode.com/problems/range-sum-query-2d-immutable/


```
Input
["NumMatrix", "sumRegion", "sumRegion", "sumRegion"]
[
  [
    [[3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]]
  ],
 [2, 1, 4, 3], [1, 1, 2, 2], [1, 2, 2, 4]
 ]

Output
[null, 8, 11, 12]

Explanation
NumMatrix numMatrix = new NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]);
numMatrix.sumRegion(2, 1, 4, 3); // return 8 (i.e sum of the red rectangle)
numMatrix.sumRegion(1, 1, 2, 2); // return 11 (i.e sum of the green rectangle)
numMatrix.sumRegion(1, 2, 2, 4); // return 12 (i.e sum of the blue rectangle)

You must design an algorithm where sumRegion works on O(1) time complexity.
```

<img src='../../assets/7_2.png'></img>

## same idea from presum

<img src='../../assets/7_3.png'></img>

base case : 右上角都是 0.0，且必須 padding 左上角的 0

<img src='../../assets/7_4.png'></img>

```python
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
      '''
      matrix = [
        [1,2,3],
        [4,5,6]
      ]
      '''
      
      height = len(matrix) # get 2
      width = len(matrix[0]) # first row of matrix, get 3
      
      self.presum_matrix : List[List[int]] = [
        [None for w in range(width + 1)]
        for h in renage(height + 1)
        ]
      
      self.presum_matrix[0][0]= 0

      for h in range(1, height + 1):
        for w in range(1, width + 1):
          self.presum_matrix[h][w] = self.presum_matrix[h - 1][w]
                               + self.presum_matrix[h][w - 1] 
                               + matrix[h - 1][w - 1] 
                               - self.presum_matrix[h - 1][w - 1] # 重複計算到的元素

      # debug
      for h in range(height+1):
        print(self.presum_matrix[h])

    def sumRegion(self, height_from: int, width_from: int, height_to: int, width_to: int) -> int:
      return self.presum_matrix[height_to + 1][width + 1] - self.presum_matrix[height_from][width + 1] - self.presum_matrix[height_to + 1][width] + self.presum_matrix[height_from][width_from]
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
```