t = int(input())
for _ in range(t):
    n,d = map(int, input().split())
    a = list(map(int, input().split()))
    i = 1
    while i < n:
        while a[i] > 0 and i <= d:
            a[0] += 1
            a[i] -= 1
            d -= i
        i += 1
    print(a[0])
