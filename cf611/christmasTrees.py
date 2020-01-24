n, m = map(int, input().split())
x = list(map(int, input().split()))
from collections import deque
dist = {}
y = []
queue = deque()
# Initialize the multi-source BFS by adding all the source vertices to the queue.
for t in x:
    dist[t] = 0
    queue.append(t)
ans = 0
while queue:
    # Process the first node in the queue i.e. place a person here if possible and add its children to the queue.
    cur = queue.popleft()
    # We are done once m people have been placed.
    if len(y) == m:
        break
    if dist[cur] > 0:
        ans += dist[cur]
        y.append(cur)
    for v in (cur-1, cur+1):
        if v not in dist:
            dist[v] = dist[cur] + 1
            queue.append(v)
print(ans)
for p in y:
    print(p, end=' ')


