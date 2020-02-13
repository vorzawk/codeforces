from math import ceil
t = int(input())
for _ in range(t):
    n,g,b = map(int, input().split())
    goodNeeded = ceil(n/2)
    if goodNeeded <= g:
        print(n)
        continue
    ans = g
    goodNeeded -= g
    minCycles = ceil(goodNeeded/g)
    ans += minCycles * (b+g)
    ans -= minCycles * g - goodNeeded
    ans = max(ans, n)
    print(ans)
    

