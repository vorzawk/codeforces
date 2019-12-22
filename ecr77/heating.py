n = int(input())
for i in range(n):
    c, s = map(int, input().split())
    ans = (c - s % c) * (s // c) ** 2 + (s % c) * (s // c + 1) ** 2
    print(ans)
