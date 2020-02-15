import string
def solve():

    def dfs(v):
        if visited[v]:
            return
        dfsOrder.append(v)
        visited[v] = True
        for u in graph[v]:
            dfs(u)
        return

    s = input()
    graph = {}
    for c in string.ascii_lowercase:
        graph[c] = set()
    oldChar = s[0]
    for c in s[1:]:
        graph[oldChar].add(c)
        graph[c].add(oldChar)
        oldChar = c

    degree = {}
    for v in graph:
        degree[v] = len(graph[v])
        if degree[v] > 2:
            print('NO')
            return

    visited = {}
    dfsOrder = []
    for v in graph:
        visited[v] = False
    for v in graph:
        if degree[v] < 2:
            dfs(v)
    for v in graph:
        if not visited[v]:
            print('NO')
            return

    print('YES')
    print(''.join(dfsOrder))

t = int(input())
for _ in range(t):
    solve()


