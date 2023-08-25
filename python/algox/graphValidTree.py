def valid_tree(es: [tuple[int, int]], n:int) -> bool:
    """
"Graph Valid Tree" is a classic graph problem that can be found on LeetCode. The problem is often used to test your understanding of graph theory and depth-first search (DFS) algorithms. The problem is described as follows:

Problem Description:
You have a graph of n nodes labeled from 0 to n - 1, and an array edges where edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph. You are also given an integer n, the number of nodes in the graph.

Write a function to check whether the graph can be represented as a single tree. A tree is a graph in which there is exactly one undirected edge between any two nodes, and there are no cycles.

Analysis:
    BFS or DFS search until done or see cycles
    """
    i0, ns = to_ns(es)
    pending = {i0}
    visited = set()
    while len(pending) > 0:
        next_level = set()
        for i in pending:
            if i in ns:
                js = ns[i]
                for j in js:
                    if j in visited:
                        return False
                    if j in pending:
                        return False
                    next_level.add(j)
                    ns[j].remove(i)
            visited.add(i)
        pending = next_level
    return len(visited) == n

def to_ns(es: [(int, int)]) -> (int, dict[int, set[int]]):
    ns = dict()
    i0 = None
    for e in es:
        (i, j) = e
        i0 = i
        if i in ns:
            ns[i].add(j)
        else:
            ns[i] = {j}
        if j in ns:
            ns[j].add(i)
        else:
            ns[j] = {i}
    return i0, ns

def valid_tree_dfs(es: [tuple[int, int]], n:int) -> bool:
    i0, ns = to_ns(es)
    pending = [i0]
    visited = set()
    while len(pending) > 0:
        i = pending[len(pending)-1]
        pending = pending[:len(pending)-1]
        visited.add(i)
        if i in ns:
            js = ns[i]
            for j in js:
                ns[j].remove(i)
                if j in visited:
                    return False
                if j in pending:
                    return False
                pending.append(j)
    return len(visited) == n


if __name__ == "__main__":
    es = [[0,1], [0,2], [0,3], [1,4]]
    # es = [[0,1], [1,2], [2,3], [1,3], [1,4]]
    n = 5
    print(valid_tree_dfs(es, n))
