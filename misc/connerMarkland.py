t = int(input())
def solve():
    n,s,k = map(int, input().split())
    closed = set(list(map(int, input().split())))
#    print(closed)
    ans = 1001
    curr = s
    cnt = 0
    while curr >= 1:
        if curr not in closed:
            ans = min(ans, cnt)
            break
        curr -= 1
        cnt += 1

    curr = s
    cnt = 0
    while curr <= n:
#        print(curr)
        if curr not in closed:
            ans = min(ans, cnt)
            break
        curr += 1
        cnt += 1

    print(ans)
    return



for _ in range(t):
    solve()
