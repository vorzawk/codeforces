t = int(input())
for _ in range(t):
    n = int(input())
    rmin = 1e9
    lmax = 0

    for _ in range(n):
        l,r = map(int, input().split())
        rmin = min(rmin, r)
        lmax = max(lmax, l)

    ans = max(0, lmax-rmin)
    print(ans)



