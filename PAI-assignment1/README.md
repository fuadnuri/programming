# PAI - Assignment I: Python Algorithmic Solutions

Welcome to the repository for **PAI - Assignment I**. This project contains Python implementations for six classic algorithmic challenges, ranging from dynamic programming to graph theory.

---

## 📋 Table of Contents

* [1. Longest Increasing Subsequence](https://www.github.com/fuadnuri/programming/assignment1/blob/main/solutions.py#L1)
* [2. Sudoku Solver](https://www.github.com/fuadnuri/programming/assignment1/blob/main/solutions.py#L1)
* [3. N-Queens Problem](https://www.github.com/fuadnuri/programming/assignment1/blob/main/solutions.py#L1)
* [4. Word Ladder](https://www.github.com/fuadnuri/programming/assignment1/blob/main/solutions.py#L1)
* [5. Median of Two Sorted Arrays](https://www.github.com/fuadnuri/programming/assignment1/blob/main/solutions.py#L1)
* [6. Graph Cycle Detection](https://www.github.com/fuadnuri/programming/assignment1/blob/main/solutions.py#L1)

---

## 🧠 Algorithms Overview

### 1. Longest Increasing Subsequence (LIS)

Find the length of the longest subsequence in an array where elements are in strictly increasing order.

* 
**Method**: Dynamic Programming.


* 
**Time Complexity**:  (optimized from ).


* 
**Key Concept**: A subsequence is derived by deleting elements without changing the order of remaining elements.



### 2. Sudoku Solver

A functional solver for a partially filled 9x9 Sudoku board.

* 
**Method**: Backtracking.


* 
**Logic**: Recursively fill empty spaces (represented by 0) with numbers 1-9 and backtrack if a placement is invalid.



### 3. N-Queens Problem

Place  queens on an  chessboard so that no two queens threaten each other.

* 
**Constraints**: No two queens can be on the same row, column, or diagonal.


* 
**Method**: Backtracking with state tracking for diagonals.



### 4. Word Ladder

Find the shortest transformation sequence from a `beginWord` to an `endWord` using a dictionary.

* 
**Rules**: Change one letter at a time; each intermediate word must be in the dictionary.


* 
**Method**: Breadth-First Search (BFS).



### 5. Median of Two Sorted Arrays

Find the median of two sorted arrays with a specific run time complexity of .

* 
**Method**: Binary Search.


* 
**Logic**: Partition the arrays such that the left and right halves are balanced.



### 6. Graph Cycle Detection

Determine if a directed graph contains a cycle.

* 
**Method**: Depth First Search (DFS).


* 
**Logic**: Use a recursion stack to track visited nodes; revisiting a node in the current stack indicates a cycle.



---

## 🛠️ Usage

This project is split into two main files for clean organization:

1. **`algorithms.py`**: Contains the logic for all six functions.
2. 
**`main.py`**: Imports the functions and runs test cases using example data provided in the assignment (e.g., LIS example array `[10, 22, 9, 33, ...]` ).



### Running the Tests

To verify the solutions, simply run the main script:

```bash
python main.py

```

---

> 
> **Note**: These solutions were developed following the specific optimization hints provided in the assignment brief, such as utilizing BFS for shortest paths and backtracking for constraint satisfaction problems.
> 
> 

Here is the updated **Complexity Analysis** section for your `README.md`. I've broken down the efficiency of each algorithm based on the methods used in the implementation.

---

## 📊 Complexity Analysis

The following table summarizes the time and space complexity for each solution. These complexities reflect the optimized approaches (Dynamic Programming, BFS, and Binary Search) suggested in the assignment hints.

| Algorithm | Method | Time Complexity | Space Complexity |
| --- | --- | --- | --- |
| **Longest Increasing Subsequence** | Dynamic Programming | <br> 

 |  |
| **Sudoku Solver** | Backtracking | <br> 

 |  |
| **N-Queens Problem** | Backtracking | <br> 

 |  |
| **Word Ladder** | Breadth-First Search | <br> 

 |  |
| **Median of Two Sorted Arrays** | Binary Search | <br> 

 |  |
| **Graph Cycle Detection** | Depth First Search | <br> 

 |  |

---

### 🔍 Deep Dive into Efficiency

* 
**Longest Increasing Subsequence**: While the brute force approach is , the Dynamic Programming approach reduces this significantly to  by storing sub-problem results.


* 
**Sudoku Solver**: Backtracking explores the state space by trying values 1-9. While the theoretical worst case is high, the "is_valid" constraints prune the search tree early.


* 
**N-Queens**: The time complexity is  because we place one queen per row and exclude occupied columns/diagonals.


* 
**Word Ladder**: Using BFS ensures the **shortest** path is found.  represents the length of the word, and  is the total number of words in the dictionary.


* 
**Median of Two Arrays**: By using Binary Search to find the correct partition point, we avoid merging the arrays, meeting the strict  requirement.


* 
**Cycle Detection**: DFS is used to traverse the graph. If a node currently in the recursion stack is encountered again, a cycle is confirmed.

