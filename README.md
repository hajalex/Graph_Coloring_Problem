# Graph Coloring Problem Solver

This Python script solves the graph coloring problem using a backtracking approach.

![Graph Coloring](https://github.com/hajalex/Graph-Coloring-Problem/assets/112249748/212d756d-bfd2-47ba-80e7-39acdb094719)

---

## Overview

This script aims to solve the classic Graph Coloring Problem by employing a backtracking algorithm. The problem revolves around coloring the nodes of a graph in such a way that no two adjacent nodes share the same color. The script achieves this through a series of functions:

- `check_valid(graph)`: This function ensures the validity of the input graph. It confirms that no node is connected to itself and guarantees that if node A is connected to node B, node B must be connected back to node A.

- `check_solution(graph, solution)`: This function validates a given coloring solution. It verifies that each node in the graph exists in the solution and that neighboring nodes have distinct colors.

- `find_best_candidate(graph, guesses)`: This function identifies the optimal node to be colored next. The selection is based on the count of previously guessed neighbors and the count of remaining neighbors. The goal is to prioritize nodes with fewer color options.

- `solve(graph, colors, guesses, depth)`: The core backtracking function attempts to find a valid coloring solution for the graph. It iterates through possible colors for the current candidate node and explores the solution space recursively. If a valid solution is found, the function returns the colored nodes; otherwise, it backtracks.

- `solve_problem(graph, colors)`: This function orchestrates the solving process. It first validates the input graph, then employs the `solve` function to find a solution, and finally confirms the solution's validity using `check_solution`.

![mapc](https://github.com/hajalex/Graph_Coloring_Problem/assets/112249748/a506a67b-64f5-4826-8049-0f140501fce2)

---

## Usage

1. Adjust the `australia` dictionary to represent the graph of Australian territories, with each territory linked to its neighboring territories.

2. Modify the `colors` list to contain the available colors for node coloring.

3. Run the script, which invokes `solve_problem` with the Australia graph and colors to find and display a valid solution. The script also reports the number of function calls made during the solving process.

---

Feel free to explore and modify the script to solve different instances of the graph coloring problem!
