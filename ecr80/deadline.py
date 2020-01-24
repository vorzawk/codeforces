from math import ceil, sqrt, floor
N = int(input())
for _ in range(N):
    n, d = map(int, input().split())
    x = sqrt(d) - 1
    x1 = ceil(x)
    days = x1 + ceil(d/(x1+1))
    if days <= n:
        print("yes")
        continue
    x2 = floor(x)
    days = x2 + ceil(d/(x2+1))
    if days <= n:
        print("yes")
        continue
    print("no")

