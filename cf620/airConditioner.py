def solve():
    n,m = map(int, input().split())
    customers = []
    for _ in range(n):
        customers.append(map(int, input().split()))
    t = 0
    mn = mx = m
    for new_t,l,h in customers:
        timeRem = new_t - t
        mn = mn - timeRem
        mx = mx + timeRem
        if mn > h or mx < l:
            print('NO')
            return
        mn = max(mn, l)
        mx = min(mx, h)
        t = new_t
    print('YES')
    return

t = int(input())
for _ in range(t):
    solve()
