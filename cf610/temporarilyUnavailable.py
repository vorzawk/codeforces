N = int(input())
for i in range(N):
    a, b, c, r = map(int, input().split())
    l = min(a, b)
    h = max(a, b)
#    print(l, h, c, r)
#    print(c-r, c+r)
    ans = h - l
    lb = max(l, c-r)
    rb = min(h, c+r)
    cs = max(0, rb - lb)
#    print(ps, cs)
    ans = ans - cs
    print(ans)

