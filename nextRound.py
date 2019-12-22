n, k = map(int, input().split())
scores = list(map(int, input().split()))
ans = 0
for s in scores:
    ans += (s > 0) and (s >= scores[k - 1])
print(ans)

