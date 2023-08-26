# graph-coloring-problem
Python script that solves a graph coloring problem using a backtracking approach

Here's an overview of what the script does:

check_valid(graph): This function is responsible for checking whether the input graph is valid. It verifies that no node is linked to itself and that if node A is linked to node B, then node B must be linked back to node A.

check_solution(graph, solution): This function checks whether a given coloring solution is valid. It ensures that each node in the graph is present in the solution and that adjacent nodes have different colors.

find_best_candidate(graph, guesses): This function finds the best candidate node to be colored next. The candidate is selected based on the number of already guessed neighbors and the number of remaining neighbors. The idea is to prioritize nodes that are likely to have fewer valid color options.

solve(graph, colors, guesses, depth): This is the main backtracking function that tries to find a valid coloring solution for the graph. It iterates through the possible colors for the current candidate node and recursively explores the solution space. If a valid solution is found, it returns the colored nodes; otherwise, it backtracks.

solve_problem(graph, colors): This function calls the above functions in sequence to solve the graph coloring problem. It first checks the validity of the input graph, then invokes the solve function to find a solution, and finally checks whether the solution is valid using check_solution.

The australia dictionary represents the graph of Australian territories, where each territory is associated with its neighboring territories.

The colors list contains the available colors for coloring the nodes.

The script then calls solve_problem with the Australia graph and colors to find and print a valid solution. It also prints the number of function calls made during the solving process.
