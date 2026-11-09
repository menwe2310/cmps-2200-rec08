from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph

def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        ###TODO
        node = frontier.pop()
        for nb in graph[node]:
            if nb not in result:
                result.add(nb)
                frontier.add(nb)
    return result

def connected(graph):
    ### TODO
    for node in graph:
        r_nodes = reachable(graph, node)
        if len(r_nodes) != len(graph):
            return False
    return True

def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    ### TODO
    nodes = list(graph.keys())
    count = 0
    while len (nodes) > 0:
        node = nodes.pop()
        r_nodes = reachable(graph, node)
        count += 1
