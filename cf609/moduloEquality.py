n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

b.sort()
ans = m
for num in a:
    x = (b[0] - num) % m
    c = [(elem+x) % m for elem in a]
    c.sort()
    if b == c:
        ans = min(x, ans)
print(ans)


