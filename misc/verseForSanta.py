t = int(input())
def solve():
    n,s = map(int, input().split())
    a = list(map(int, input().split()))
    maxId = -1
    maxVerse = 0
    i = 0
    while i < n and s >= 0:
        s -= a[i]
        if a[i] > maxVerse:
            maxId = i
            maxVerse = a[i]
        i += 1
    if i == n:
        print(0)
        return
    print(maxId + 1)

for _ in range(t):
    solve()




