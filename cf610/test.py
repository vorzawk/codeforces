N = int(input())
for _ in range(N):
    n, p, k = map(int, input().split())
    ap = p
    items = list(map(int, input().split()))
    items.sort()
    ans = 0
    for i in range(1,n,2):
        if items[i] <= p:
            ans += 2
            p -= items[i]
        else:
            break
    if items[i-1] <= p:
        ans += 1
    aans = 0
    for i in range(2,n,2):
        if items[i] <= ap:
            aans += 2
            ap -= items[i]
        else:
            break
    if items[0] <= ap:
        aans += 1
 
    ans = max(ans, aans)
    print(ans)
