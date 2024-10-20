# Ref

https://github.com/labuladong/fucking-algorithm

* 對岸大佬 : 刷的是題，練的是思維，從思維層面重新解構 leetcode 刷題

# Compare to 

[blind75](https://ithelp.ithome.com.tw/articles/10287061)

* 美國大佬 : 相似概念，常見的資料結構和演算法精選題，並按照資料結構、演算法來分類

# Memo

在大廠軟體工程師面試中，LeetCode 題目的回答標準不僅關乎正確性，還要展示出對問題的理解和解決問題的過程。以下是面試中應答 LeetCode 題目時應遵循的標準流程與技巧：

1. 理解問題
Clarify the question：當面試官提出問題時，務必確保自己完全理解問題的要求。你可以總結題意或向面試官確認一些細節，避免誤解題目。這個步驟可以展示出你的溝通能力。
Identify edge cases：主動提出可能的邊界情況（例如，空輸入、極端數值等），這不僅能展現你的全面性，也顯示你對應用場景的敏銳度。
2. 初步思考與計畫
Think aloud：面試官通常希望你能“思考過程公開化”，也就是邊思考邊說出你對問題的分析，例如可能的數據結構和算法選擇。這能讓面試官看到你的解題思路，而不僅僅是最後的答案。
Discuss multiple approaches：不一定直接選擇最佳解法，可以先討論幾種不同的策略，例如暴力解法、再逐步優化。這能展示你的問題分解能力。
3. 解法設計
Choose an optimal approach：在討論不同方法後，選擇一個最合適的解法，並闡述為什麼選這種方法。記得提及時間複雜度和空間複雜度，這是面試官特別關注的點。
Pseudocode first：可以先用偽代碼或高階步驟描述解法，再進入具體的程式碼撰寫。這樣可以更清晰地展示你的解題框架，減少細節錯誤。
4. 撰寫程式碼
Write clean code：程式碼必須清晰、結構化。變數命名要具體並具描述性，並遵循常見的編碼風格。這可以展示出你良好的程式設計能力。
Focus on correctness：撰寫程式時，確保邏輯正確無誤。可以適時停下來檢查一下自己寫的程式碼，避免低階錯誤。
Handle edge cases：在程式碼中處理你先前提到的邊界情況，讓面試官看到你對全面性和健壯性的重視。
5. 測試與調試
Test with examples：在完成程式碼後，使用幾個測試例子來驗證。這包括給出簡單例子和邊界情況的測試，顯示你在驗證和確保程式碼的正確性。
Debug if necessary：如果測試失敗，展示你如何有效地調試程式碼。面試官希望看到你能冷靜地排除問題並做出修正。
6. 複雜度分析與優化
Discuss time/space complexity：在程式碼撰寫完畢後，主動分析你的解法的時間複雜度和空間複雜度，這通常是 O(n)、O(log n) 或 O(n^2) 的分析，展示你對算法效能的理解。
Suggest optimizations：如果有時間且適當，可以提議一些進一步的優化方案，即使你選擇的已經是最佳解法，這能顯示你解題的深度思考。
7. 態度與心態
Stay calm and positive：保持冷靜，若遇到不確定的地方，也不必慌張。可以坦然表示自己的想法並請教面試官。這樣的互動可以增加面試的合作感，展現你的抗壓能力。
Be adaptable：如果面試官要求更改或進一步優化解法，展示你靈活應對的能力，不要執著於某個解法而無法調整。
總結來說，LeetCode 題目面試的標準不僅關注正確答案，更看重解題思路、與面試官的互動、代碼質量、複雜度分析和優化能力。掌握這些應對技巧，可以幫助你在大廠面試中脫穎而出。


"""
1. claasifiy questions
    so let me repeat the questions again if you don't mind
    - all the element in the array is a number
    - the follow a ascending orders
    - the target must be the elements add up, and only 2 elements to achieve that
    - follow up - what if the target could get multiple answer pair?
    - follow up - what if the target doesn't match any awerser pair?
    - return the index, not the actual elements

2. So, for this kind of problem, there are several approaches to solve
    - one of the most simple approach is use 2 for loops, for each loop, we could loop over the array and get almost N*N combinations, 
    once the element add up equal the target number, then we get a solution pair, let's 1
        TC : O(N^2)
        SC : O(1)
    - and since the first approach is kind of brute force, we could build up a hash table for the repeating search, let's say,
    we do first loop to build up a hashtable, key = elements, value = index
    second loop is that, we loop over the numbers, get elements, perform target-element as remind, 
    to check whatever the remind is in the hash-table as key (O(1)), if exist, we get the solution pair
        TC : O(2N) ~ O(N)
        Sc : O(N)
    - the third approach is optimized from sol2, since we need to build a hash table for all elements, it's will cost space complexity O(N)
    However, the elements in the array is sorted, so we could achieve it with space complexity O(1), time complexity O(N), we could try a 
    binary-search-like approach
    we use two pointer, left, right, left starts from zero, right starts from the end of the array, we perform an add operations for two elements, 
    if add up equal to tatget, then solved, if add up less than to that target, we need to make the add up value greater, by the sorted nautre of this questions, 
    left index need to add 1, let's say, left += 1, then we'll get a grater add on values, then perform the checking.
    on the other hand, if thre add up values greater than the targets, we need to make the add up value smaller, by the sorted critiria, we could make
    right index shift to the left, let's say, right -= 1, them perform the checking again, by that, if the solution exist, we may get the solution pair in O(N)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # test case : [2,7,11,15], target = 9
        left, right = 0, len(numbers) - 1
        while left > right:
            # cross over is the fully loop over critirial
            add_up = numbers[left] + numbers[right]
            # 2+15 = 17
            # 2+11 = 13
            # 2+7 = 9
            if target == add_up:
                # there is a index padding I noticed
                return [left+1, right+1] 
            elif target >= add_up:
                # add_up need to grater
                left += 1
            else:
                # left from 3 to 2
                # left from 2 to 1
                left -= 1