N = int(input())
for _ in range(N):
    a, b, c = map(int, input().split())
    ans = 1e10
    for i in range(a - 1, a + 2):
        for j in range(b - 1, b + 2):
            for k in range(c - 1, c + 2):
                d = abs(i - j) + abs(j - k) + abs(i - k)
                ans = min(ans, d)
    print(ans)
