
def course_sched(deps: dict[int,[int]]) -> bool:
    """
    There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.



Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take.
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
   
   Analysis:
   Just a topology sort. Nodes with zero deps are picked first, then remove it from rest of deps.
    """
    processed = set()
    while len(deps) > 0:
        cyclic = True
        for i in deps:
            if len(deps[i]) == 0:
                cyclic = False
                deps.pop(i)
                processed.add(i)
                for j in deps:
                    if i in deps[j]: deps[j].remove(i)
                break
        if cyclic:
            return False
    return True


def rel_to_adjs(pairs: [[int]]) -> dict[int, [int]]:
    deps = dict()
    for pair in pairs:
        i = pair[0]
        dep = deps.get(i, None)
        if dep is None:
            dep = []
            deps[i] = dep
        j = pair[1]
        dep.append(j)
        if not j in deps:
            deps[j] = []
    return deps


if __name__ == "__main__":
    rel = [[1,0],[0,1]]
    # rel =  [[1,0]]
    deps = rel_to_adjs(rel)
    print("deps: ", deps)
    print(course_sched(deps))
