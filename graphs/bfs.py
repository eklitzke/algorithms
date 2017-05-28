"""Basic BFS implementation."""


def visit(graph, current, visited, queue):
    for node in graph[current]:
        if node not in visited:
            queue.append(node)
            visited.add(node)
    if queue:
        head = queue.pop(0)
        print('visiting {}'.format(head))
        visit(graph, head, visited, queue)


def bfs(graph, start):
    print('starting at {}'.format(start))
    visited = {start}
    queue = []
    visit(graph, start, visited, queue)


def test():
    graph = {'A': set(['B', 'C']),
             'B': set(['A', 'D', 'E']),
             'C': set(['A', 'F']),
             'D': set(['B']),
             'E': set(['B', 'F']),
             'F': set(['C', 'E'])}

    bfs(graph, 'A')
