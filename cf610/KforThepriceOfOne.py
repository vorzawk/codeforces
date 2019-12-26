N = int(input())
for _ in range(N):
    n, p, k = map(int, input().split())
    items = list(map(int, input().split()))
    items.sort()
    ans = 0
    prefix = 0
    for i in range(k):
        # i is the number of items in the optimal solution bought without the offer, 0 <= i <= k-1
        if i > 0:
            prefix += items[i-1]
        cost = prefix
        if cost <= p:
            cnt = i
            for j in range(i+k-1, n, k):
                if cost + items[j] <= p:
                    cost += items[j]
                    cnt += k
                else:
                    break
        ans = max(cnt, ans)
    print(ans)

