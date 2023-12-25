from itertools import combinations


# get all edges
# iterate over all cominations with 3 missing
# convert combination to adj list graph
# count disconnected components and keep track of their sizes
# if there are 2 disconnected components, return their product


def edges_to_graph(edges):
    graph = {}
    for edge in edges:
        for node in edge:
            if node not in graph:
                graph[node] = []
            graph[node].append(next(iter(edge - {node})))
    return graph

def count_disconnected_components(graph):
    def dfs(node, visited):
        visited.add(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor, visited)
    
    visited = set()
    first = list(graph.keys())[0]
    dfs(first, visited)
    first_size = len(visited)

    for node in graph.keys():
        if node not in visited:
            new_visited = set()
            dfs(node, new_visited)
            second_size = len(new_visited)
            if first_size + second_size == len(graph.keys()):
                return first_size * second_size
            else:
                return None
    return None

with open("input2") as f:
    # get all edges
    lines = f.read()

    def parse_input(input_string):
        # Parse the input string to build the graph
        graph = {}
        for line in input_string.split('\n'):
            if line:
                node, neighbors = line.split(':')
                graph[node.strip()] = neighbors.split()

        return graph

    graph = parse_input(lines)
    edges = []

    for node in graph.keys():
        for neighbor in graph[node]:
            edge_set = set()
            edge_set.add(node)
            edge_set.add(neighbor)
            edges.append(edge_set)
    
    # iterate over all cominations with 3 missing
    sel_count = len(edges) - 3

    for comb in combinations(edges, sel_count):
        # convert combination to adj list graph
        graph = edges_to_graph(comb)

        # count disconnected components and keep track of their sizes
        res = count_disconnected_components(graph)

        if res != None:
            print(res)
            break
            