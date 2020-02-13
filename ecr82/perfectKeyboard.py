import string
t = int(input())
for _ in range(t):
    ok = True
    s = input()
    graph = {}
    for c in string.ascii_lowercase:
        graph[c] = set()
    oldChar = s[0]
    for c in s[1:]:
        graph[oldChar].add(c)
        graph[c].add(oldChar)
        oldChar = c
#    print(graph)
    degree = {}
    for v in graph:
        degree[v] = len(graph[v])
        if degree[v] > 2:
            ok = False
            break
    if not ok:
        print('NO')
        continue
#    print(degree)
    visited = {}
    dfsOrder = []
    for v in graph:
        visited[v] = False
    def dfs(v):
        if visited[v]:
            return
        dfsOrder.append(v)
        visited[v] = True
        for u in graph[v]:
            dfs(u)
    for v in graph:
        if degree[v] < 2:
            dfs(v)
    for v in graph:
        if not visited[v]:
            ok = False
            break

    if not ok:
        print('NO')
        continue

    print('YES')
    print(''.join(dfsOrder))





