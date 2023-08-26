def check_valid(graph):
    for node, nexts in graph.items():
        assert (node not in nexts)  # no node linked to itself
        for next in nexts:
            # A linked to B implies B linked to A
            assert (next in graph and node in graph[next])


def check_solution(graph, solution):
    if solution is not None:
        for node, nexts in graph.items():
            assert node in solution, f"Node {node} is missing from solution."
            color = solution[node]
            for next_node in nexts:
                assert next_node in solution and solution[
                    next_node] != color, f"Adjacent nodes {node} and {next_node} have the same color."


def find_best_candidate(graph, guesses):
    candidates_with_add_info = [
        (
            -len({guesses[neigh]
                 for neigh in graph[node] if neigh in guesses}),
            -len({neigh for neigh in graph[node] if neigh not in guesses}),
            node
        ) for node in graph if node not in guesses]
    candidates_with_add_info.sort()
    candidates = [n for _, _, n in candidates_with_add_info]
    if candidates:
        candidate = candidates[0]
        assert candidate not in guesses, f"Node {candidate} is already guessed."
        return candidate
    assert set(graph.keys()) == set(guesses.keys()), "Solution not found."
    return None


nb_calls = 0


def solve(graph, colors, guesses, depth):
    global nb_calls
    nb_calls += 1
    n = find_best_candidate(graph, guesses)
    if n is None:
        return guesses
    for c in set(colors).difference({guesses[neigh] for neigh in graph[n] if neigh in guesses}):
        if n not in guesses:
            assert all(guesses[neigh] !=
                       c for neigh in graph[n] if neigh in guesses)
            guesses[n] = c
            indent = '  ' * depth
            print(f"{indent}Trying to give color {c} to {n}")
            if solve(graph, colors, guesses, depth + 1):
                print(f"{indent}Gave color {c} to {n}")
                return guesses
            else:
                del guesses[n]
                print(f"{indent}Cannot give color {c} to {n}")
    return None


def solve_problem(graph, colors):
    check_valid(graph)
    solution = solve(graph, colors, dict(), 0)
    print(solution)
    check_solution(graph, solution)


WA = 'western australia'
NT = 'northwest territories'
SA = 'southern australia'
Q = 'queensland'
NSW = 'new south wales'
V = 'victoria'
T = 'tasmania'

australia = {T:   {V},
             WA:  {NT, SA},
             NT:  {WA, Q, SA},
             SA:  {WA, NT, Q, NSW, V},
             Q:   {NT, SA, NSW},
             NSW: {Q, SA, V},
             V:   {SA, NSW, T}}


colors = ['red', 'green', 'blue', 'yellow']

solve_problem(australia, colors)

print(nb_calls)
