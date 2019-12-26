N = int(input())
a = list(map(int, input().split()))

l = [1] * N
r = [1] * N
ans = 1

for i in range(1, N):
    if a[i] > a[i-1]:
        l[i] = l[i-1] + 1
        ans = max(l[i], ans)

for i in range(N-2, -1, -1):
    if a[i] < a[i+1]:
        r[i] = r[i+1] + 1
        ans = max(r[i], ans)

for i in range(N-2):
    if a[i] < a[i+2]:
        ans = max(ans, l[i] + r[i+2])

print(ans)


