def solve():
    times = []
    high = []
    low = []
    n,m = map(int, input().split())
    for _ in range(n):
        t,l,h = map(int, input().split())
        times.append(t)
        high.append(h)
        low.append(l)

#    print(times, low, high)
    t = m
    curr = 0
    for i in range(n):
#        print(curr, t)
        j = i
        while j < n and low[j] <= t <= high[j]:
            j += 1
        if j < n and t < low[j]:
            if low[j] - t <= times[j] - curr:
                if t+1 <= high[i]:
                    t += 1
                curr += 1
            else:
                print('NO')
                return
        elif j < n and t > high[j]:
            if t - high[j] <= times[j] - curr:
                if t-1 >= low[i]:
                    t -= 1
                curr += 1
            else:
                print('NO')
                return
        else:
            curr += 1
    print('YES')
    return


t = int(input())
for _ in range(t):
    solve()
