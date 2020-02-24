t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(lambda x: int(x) - 1, input().split()))
    ans = [-1] * n
    for i in range(n):
        if ans[i] == -1:
            cycle = set()
            u = i
            while u not in cycle:
                cycle.add(u)
                u = p[u]
            for u in cycle:
                ans[u] = len(cycle)
    for elem in ans:
        print(elem, end = ' ')
    print()



