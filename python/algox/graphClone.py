def graph_clone(node: dict) -> dict:
    """
    Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}


Test case format:

For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.

An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.

The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.

Analysis:
BFS search.
Verify:
BFS for both original and cloned graph, check values are the same but references are different.
    """
    orig_nodes = dict()
    pending = [node]
    cloned_nodes = dict()
    while len(pending) > 0:
        curr = pending[0]
        pending = pending[1:]
        val = curr["val"]
        cloned_curr = cloned_nodes.get(val, None)
        orig_nodes[val] = curr
        if cloned_curr is None:
            new_node = {"val": val, "adj": []}
            cloned_nodes[val] = new_node
        for adj_node in curr["adj"]:
            tmp_val = adj_node["val"]
            tmp = cloned_nodes.get(tmp_val, None)
            if tmp is None:
                # not cloned yet
                pending.append(adj_node)
    for val in cloned_nodes:
        orig_node = orig_nodes[val]
        cloned_node = cloned_nodes[val]
        for adj in orig_node["adj"]:
            adj_val = adj["val"]
            cloned_node["adj"].append(cloned_nodes[adj_val])
    return cloned_nodes


if __name__ == "__main__":
    n1 = {"val": 1}
    n2 = {"val": 2}
    n3 = {"val": 3}
    n4 = {"val": 4}
    n1["adj"] = [n2, n4]
    n2["adj"] = [n1, n3]
    n3["adj"] = [n2, n4]
    n4["adj"] = [n1, n3]
    print(graph_clone(n1))
