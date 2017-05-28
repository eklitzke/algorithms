"""Basic DFS implementation."""


def visit(graph, current, visited):
    for node in graph[current]:
        if node in visited:
            continue
        print('visited {}'.format(node))
        visited.add(node)
        visit(graph, node, visited)


def dfs(graph, start):
    visited = {start}
    print('starting at {}'.format(start))
    visit(graph, start, visited)


def test():
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}

    dfs(graph, 'A')
