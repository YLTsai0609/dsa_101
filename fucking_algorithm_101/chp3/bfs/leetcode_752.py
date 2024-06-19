# Definition for a binary tree node.
# https://leetcode.com/problems/open-the-lock/description/

from typing import Optional, List
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 將 s[j] 往上撥
def plus_one(s : str, j : str) -> str:
    ch = list(s)
    if ch[j] == '9':
        ch[j] == '0'
    else:
        ch[j] = str(int(ch[j]) + 1)
    return ''.join(ch)

# 將 s[j] 往下撥
def minus_one(s : str, j : str) -> str:
    ch = list(s)
    if ch[j] == '0':
        ch[j] = '9'
    else:
        ch[j] = str(int(ch[j]) - 1)
    return ''.join(ch)


def BFS_v1(target : str) -> int:
    '''
    1. 可以回傳 steps
    2. 但是會產生無窮迴路 --> 0000 --> 1000 --> 又回到 0000
    3. 還沒有避開 depends (deadlock)
    '''
    q = ['0000']
    step = 0
    while len(q) > 0:
        size = len(q)
        # 從節點向外擴散
        for i in range(size):
            cur = q.pop(0) # 把 string pop 出來

            if cur == target:
                return step
            # 節點探索，每個數字兩個，總共 8 個
            for j in range(4):
                up = plus_one(cur, j)
                down = minus_one(cur, j)
                q.append(up)
                q.append(down)
            step += 1

def BFS_v2(deadends : List[str],target : str, verbose : bool = True) -> int:
    '''
    tc ?
    sc ?
    步數
    節點數
    '''
    # 記錄需要跳過的死亡密碼
    deads = set(deadends)

    # 紀錄已經走過的節點，可以跳過他們
    visisted = set()
    q = deque()
    step = 0
    
    q.append('0000')
    visisted.add('0000')
    for dead in deadends:
        visisted.add(dead)

    while q:
        n_nodes = len(q) # 目前有的節點數量，開始做 BFS
        for _ in range(n_nodes):
            cur = q.popleft()

            # 到達 target / deadlock 都跳過
            if cur in deads:
                continue
            if cur == target:
                return step
            
            # explore the next nodes
            for j in range(4):
                up = plus_one(cur, j)
                # 回頭路不走
                if up not in visisted:
                    q.append(up)
                    visisted.add(up)
                down = minus_one(cur, j)
                # 回頭路不走
                if down not in visisted:
                    q.append(down)
                    visisted.add(down)
        step += 1
        if verbose:
            print(f'step = {step}, queue : {q}, visited : {visisted}')
    return -1


def Bidirection_BFS(deadends : List[str],target : str, verbose : bool = True) -> int:
    '''
    雙向 BFS
    從 source, target 兩個點各自向外做 BFS，在各自的 BFS 節點相遇時停止
    理論上會少一半的時間，但時空複雜度不變
    '''
    deads = set(deadends)
    q1, q2 = set(), set()
    visited = set()
    step = 0
    
    # 兩個 queue 存不同的資訊
    q1.add('0000')
    q2.add(target)

    while q1 and q2:
        # 儲存下一層的狀態
        temp = set()
        for cur in q1:

            # 是否遇到 dead
            if cur in deads:
                continue
            # 是否在另一個被搜尋到的位置中
            if cur in q2:
                return step
            visited.add(cur)

            # 探索節點
            for j in range(4):
                up = plus_one(cur, j)
                if up not in visited:
                    temp.add(up)
                down = minus_one(cur, j)
                if down not in visited:
                    temp.add(down)
        step += 1
        # 交換 queue
        # q2 原本為 target, 會變成 q1，進行節點探索
        q1, q2 = q2, temp
        if verbose:
            print(f'step = {step}, q1 = {q1}, q2 = {q2}, visited = {visited}')
    return -1


questions = [
    ('0202', ["0201","0101","0102","1212","2002"], 6),
    ('0009', ["8888"], 1),
    ('8888',["8887","8889","8878","8898","8788","8988","7888","9888"], -1)
]

for q in questions:
    target, deadends, ans = q
    # print(target, deadends,ans)
    for _func in [BFS_v2, Bidirection_BFS]:
    # min_steps = BFS_v2(deadends, target, verbose=False)
        min_steps = _func(deadends, target, verbose=False)
        print(min_steps)

