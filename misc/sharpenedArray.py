t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    l = -1
    for i in range(n):
        if a[i] < i:
            break
        l += 1
    r = -1
    for i in range(n):
        if a[n-i-1] < i:
            break
        r += 1
    if r+1+l+1 >= n+1:
        print('YES')
    else:
        print('NO')

