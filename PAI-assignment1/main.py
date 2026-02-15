from solutions import (
    longest_subsequence, sodoku_solver, solve_n_quens, 
    word_ladder_length, find_median_sorted_arrays, has_cycle
)

def main():
    print("--- 1. Longest Increasing Subsequence ---")
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    print(f"Input: {arr}\nOutput: {longest_subsequence(arr)}\n")

    print("--- 2. Sudoku Solver ---")
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0], [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0], [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1], [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0], [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    if sodoku_solver(board):
        print("Sudoku Solved: True")
        for row in board: print(row)
    print()

    print("--- 3. N-Queens (N=4) ---")
    n_queens_solutions = solve_n_quens(4)
    print(f"One solution: {n_queens_solutions[0]}\n")

    print("--- 4. Word Ladder ---")
    b, e = "hit", "cog"
    w_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(f"Shortest path length: {word_ladder_length(b, e, w_list)}\n")

    print("--- 5. Median of Two Sorted Arrays ---")
    n1, n2 = [1, 3], [2]
    print(f"Median: {find_median_sorted_arrays(n1, n2)}\n")

    print("--- 6. Graph Cycle Detection ---")
    graph = {0: [1], 1: [2], 2: [3], 3: [0]}
    print(f"Cycle detected: {has_cycle(graph)}\n")

if __name__ == "__main__":
    main()