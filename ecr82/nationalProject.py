t = int(input())
for _ in range(t):
    n,g,b = map(int, input().split())
    goodNeeded = (n+1) // 2
    totalG = (goodNeeded // g) * (b+g)
    if goodNeeded % g == 0:
        totalG -= b
    else:
        totalG += goodNeeded % g
    ans = max(totalG, n)
    print(ans)
    

