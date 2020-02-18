t = int(input())
def solve():
    n,s,k = map(int, input().split())
    closed = set(list(map(int, input().split())))
    i = 0
    for i in range(k+1):
        if s-i >= 1 and s-i not in closed:
            print(i)
            break
        if s+i <= n and s+i not in closed:
            print(i)
            break
    return

for _ in range(t):
    solve()
