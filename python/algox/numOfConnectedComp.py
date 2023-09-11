def bfs(g):
    visited = set()
    if len(g) == 0:
        return visited
    q = []
    for k in g:
        q.append(k)
        break
    while len(q) > 0:
        head = q[0]
        q = q[1:]
        if head in visited:
            continue
        visited.add(head)
        adjs = g[head]
        for a in adjs:
            if not a in visited:
                q.append(a)
                if a in g:
                    if head in g[a]:
                        g[a].remove(head)
        g.pop(head)
    return visited
        

def num_of_connected(g: dict[int, [int]]) -> int:
    """
    Number of Connected Components in an Undirected Graph 
    
    Analysis:
    a BFS or DFS will navigate a connected component.
    So total cost is V+E
    """
    c = 0
    while len(g) > 0:
        visited = bfs(g)
        c += 1
    return c


def edges_to_adjs(es, n):
    g = {}
    for e in es:
        (a, b) = e
        if a in g:
            g[a].append(b)
        else:
            g[a] = [b]
        if b in g:
            g[b].append(a)
        else:
            g[b] = [a]

    for i in range(n):
        if not i in g:
            g[i] = []
    return g


if __name__ == '__main__':
    es = [(1, 2), (1,0), (3, 4)]
    n = 6
    g = edges_to_adjs(es, n)
    print(num_of_connected(g))
    
