from typing import List, Dict 

#Longest increasing subsequence
def longest_subsequence(nums:List[int])->int:
    if not nums:
        return 0
    dp=[1]*len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i]>nums[j]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)

#Sodoku solver
def sodoku_solver(board:List[List[int]])->bool:
    def is_valid(row:int,col:int,val:int)->bool:
        for i in range(9):
            if board[row][i]==val or board[i][col]==val:
                return False
            if board[3*(row//3)+i//3][3*(col//3)+i%3]==val:
                return False
        return True
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                for val in range(1,10):
                    if is_valid(r,c,val):
                        board[r][c]=val
                        if sodoku_solver(board):
                            return True
                        board[r][c]=0
                return False
    return True

#N-quens problem
def solve_n_quens(n:int)->List[List[int]]:
    result=[]
    cols=set()
    pos_diags=set()
    neg_diags=set()
    board=[-1]*n 

    def backtrack(r):
        if r == n:
            result.append(list(board))
            return 

        for c in range(n):
            if c in cols or (r+c) in pos_diags or (r-c) in neg_diags:
                continue
            cols.add(c)
            pos_diags.add(r+c)
            neg_diags.add(r-c)
            board[r]=c

            backtrack(r+1)

            #remove for backtracking
            cols.remove(c)
            pos_diags.remove(r+c)
            neg_diags.remove(r-c)
    backtrack(0)
    return result   

#Word ladder
from collections import deque

def word_ladder_length(beginWord:str,endWord:str,wordList:List[str])->int:
    wordSet = set(wordList) # Efficient lookup [cite: 46]
    if endWord not in wordSet:
        return 0
    
    queue = deque([(beginWord, 1)])
    visited = {beginWord} # Avoid cycles [cite: 55]
    
    while queue:
        word, length = queue.popleft()
        if word == endWord:
            return length
        
        for i in range(len(word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                next_word = word[:i] + char + word[i+1:]
                if next_word in wordSet and next_word not in visited:
                    visited.add(next_word)
                    queue.append((next_word, length + 1))
    return 0

#Find median of two sorted arrays
def find_median_sorted_arrays(nums1:List[int],nums2:List[int])->float:
    if len(nums1)>len(nums2):
        return find_median_sorted_arrays(nums2,nums1)
    x,y=len(nums1),len(nums2)
    low,high=0,x

    while low<=high:
        partitionX=(low+high)//2
        partitionY=(x+y+1)//2-partitionX

        max_left_x = float('-inf') if partitionX==0 else nums1[partitionX-1]
        min_right_x = float('inf') if partitionX==x else nums1[partitionX]

        max_left_y = float('-inf') if partitionY==0 else nums2[partitionY-1]
        min_right_y = float('inf') if partitionY==y else nums2[partitionY]

        if max_left_x<=min_right_y and max_left_y<=min_right_x:
            if (x+y)%2==0:
                return (max(max_left_x,max_left_y)+min(min_right_x,min_right_y))/2
            else:
                return max(max_left_x,max_left_y)
        elif max_left_x>min_right_y:
            high=partitionX-1
        else:
            low=partitionX+1
        

#Graph cycle detection
def has_cycle(graph:Dict[int,List[int]])->bool:
    visited = set()
    rec_stack = set()


    def dfs(node):
        visited.add(node)
        rec_stack.add(node)

        for neighbor in graph.get(node,[]):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        rec_stack.remove(node)
        return False
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True 
    return False

        