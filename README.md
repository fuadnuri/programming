# PAI - Assignment I: Python Algorithmic Solutions

This repository contains Python implementations for six fundamental algorithmic challenges, ranging from dynamic programming and backtracking to graph theory and binary search. [cite_start]Each solution is optimized based on the constraints and hints provided in the assignment [cite: 1-80].

---

## 📋 Table of Contents
* [1. Longest Increasing Subsequence](#1-longest-increasing-subsequence)
* [2. Sudoku Solver](#2-sudoku-solver)
* [3. N-Queens Problem](#3-n-queens-problem)
* [4. Word Ladder](#4-word-ladder)
* [5. Median of Two Sorted Arrays](#5-median-of-two-sorted-arrays)
* [6. Graph Cycle Detection](#6-graph-cycle-detection)
* [7. Complexity Analysis](#-complexity-analysis)

---

## 🧠 Algorithms Overview

### 1. Longest Increasing Subsequence (LIS)
[cite_start]Find the length of the longest subsequence in an array where elements are in strictly increasing order[cite: 3].
* [cite_start]**Method**: Dynamic Programming[cite: 9].
* [cite_start]**Time Complexity**: $O(n^2)$ (optimized from brute force $O(2^n)$)[cite: 9].



### 2. Sudoku Solver
[cite_start]A backtracking-based function that fills a 9x9 Sudoku board[cite: 12].
* [cite_start]**Method**: Backtracking[cite: 28].
* [cite_start]**Logic**: Recursively tries numbers 1-9 in empty spaces and backtracks if the placement is invalid[cite: 28, 29].



### 3. N-Queens Problem
[cite_start]Places $N$ queens on an $N \times N$ chessboard such that no two queens threaten each other[cite: 32].
* [cite_start]**Method**: Backtracking[cite: 41].
* [cite_start]**Constraints**: Queens cannot share the same row, column, or diagonal[cite: 33].



### 4. Word Ladder
[cite_start]Finds the shortest transformation sequence from a `beginWord` to an `endWord`[cite: 44].
* [cite_start]**Method**: Breadth-First Search (BFS)[cite: 53].
* [cite_start]**Logic**: Each word is a node, and each single-letter change forms an edge in the transformation graph[cite: 54].



### 5. Median of Two Sorted Arrays
[cite_start]Calculates the median of two sorted arrays with a strict runtime complexity of $O(\log(\min(n, m)))$[cite: 58, 59].
* [cite_start]**Method**: Binary Search[cite: 65].

### 6. Graph Cycle Detection
[cite_start]Determines if a directed graph contains a cycle[cite: 68].
* [cite_start]**Method**: Depth First Search (DFS)[cite: 79].
* [cite_start]**Logic**: Uses a recursion stack to track the current path; a cycle is detected if a node in the stack is revisited[cite: 79, 80].



---

## 📊 Complexity Analysis

The following table summarizes the time and space complexity for each solution provided in this repository.

| Algorithm | Method | Time Complexity | Space Complexity |
| :--- | :--- | :--- | :--- |
| **Longest Increasing Subsequence** | Dynamic Programming | $O(n^2)$ | $O(n)$ |
| **Sudoku Solver** | Backtracking | $O(9^{N^2})$ | $O(N^2)$ |
| **N-Queens Problem** | Backtracking | $O(N!)$ | $O(N)$ |
| **Word Ladder** | BFS | $O(M^2 \times N)$ | $O(M \times N)$ |
| **Median of Two Sorted Arrays** | Binary Search | $O(\log(\min(n, m)))$ | $O(1)$ |
| **Graph Cycle Detection** | DFS | $O(V + E)$ | $O(V)$ |

*Note: $N$ is the board size, $M$ is word length, $V$ is vertices, and $E$ is edges.*

---

## 🛠️ Usage

1. **`algorithms.py`**: Contains all implementation logic.
2. [cite_start]**`main.py`**: Runs test cases using example data (e.g., LIS array `[10, 22, 9, 33, ...]` [cite: 6]).

To run the project:
```bash
python main.py