N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    c = 10
    ans = 0
    while c-1 <= b:
        ans += a
        c *= 10
    print(ans)

