t = int(input())
for _ in range(t):
    c,m,x = map(int, input().split())
    if x >= min(c,m):
        print(min(c,m))
        continue
    ans = x
    c -= x
    m -= x
    if max(c,m) <= 2*min(c,m):
        ans += (c+m)//3
    else:
        ans += min(c,m)
    print(ans)
