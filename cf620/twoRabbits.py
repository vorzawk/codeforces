t = int(input())
for _ in range(t):
    ans = -1
    x,y,a,b = map(int, input().split())
    if (y-x) % (a+b) == 0:
        ans = (y-x)//(a+b)
    print(ans)

