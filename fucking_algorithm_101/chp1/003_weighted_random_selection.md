# Ref

* [带权重的随机选择算法](https://labuladong.github.io/algo/2/20/30/)

# 緣起

LOL 手遊 - 系統配對的隊友太廢 --> 系統如何排定隊友?

配對機制是所有競技類遊戲的核心環節，必定非常複雜，那麼對應上的資料結構會是什麼?

長度為 `n` 的 array，隨機選取，那麼每個 elements 被選到的機率是 `1/n`

# leetcode 528 - 按照權重隨機選擇

https://leetcode.com/problems/random-pick-with-weight/


## 回顧隨機算法

1. 設計隨機取得元素，新增、刪除在常數時間複雜度 - 主要是資料結構的應用，每次把 elements 搬到 array 尾巴再刪掉
2. [遊戲中的隨機算法](https://labuladong.github.io/algo/4/32/114/) - 水塘抽樣算法，運用數學運算，在無限序列中等機率選取元素
  
但能解決目前問題的，反而是 `前綴和`, `binary search`

...