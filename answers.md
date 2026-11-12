# CMPS 2200 Recitation 08 Answers

**Name:** Menwe Okafor
**Name:**_________________________


Place all written answers from `recitation-10.md` here for easier grading.


- **2) (2 pts)** What is the work of `reachable`, assuming $n$ nodes and $m$ edges?
    O(n + m). Each node is added to the frontier at most once, and each edge gets checked at most twice (once from each end).


- **4) (1 pt)** What is the worst case number of times we need to call `reachable` to determine if a graph is connected?
     1: In an undirected graph, if one node can reach every other node, then every node can reach every other one by going through it. So one call to `reachable` from any node tells us if the whole graph is connected.

- **5) (2 pts)** What is the work of `connected`, assuming $n$ nodes and $m$ edges?
    O(n(n + m)). It calls `reachable` up to n times, and each call is O(n + m).

- **7) (1 pt)** What if we switched the graph representation to an adjacency matrix? Would the work of `reachable` change? If so, what would it be? If not, why not?
    Yes, it becomes O(n²). Finding a node's neighbors in a matrix means scanning its whole row of n entries, and we do that for all n nodes.
