N = int(input())
ans = 0
for i in range(N):
    p = map(int, input().split())
    ans += sum(p) >= 2
print(ans)
