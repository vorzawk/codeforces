n = int(input())
managers = [-1] * n
for i in range(n):
    manager = int(input())
    if manager != -1:
        managers[i] = manager - 1

tree = {}
for i in range(n):
    tree[i] = []
for i,m in enumerate(managers):
    if m != -1:
        tree[m].append(i)

def largestChain(v):
    if not tree[v]:
        return 1
    ans = 0
    for u in tree[v]:
        ans = max(ans, largestChain(u) + 1)
    return ans

ans = 0
for i in range(n):
    if managers[i] == -1:
        ans = max(ans, largestChain(i))
print(ans)
