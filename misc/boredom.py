N = int(input())
a = list(map(int, input().split()))
freq = {}
for e in a:
    if e not in freq:
        freq[e] = 0
    freq[e] += 1
a = list(set(a))
a.sort()
n = len(a)
res = [None] * (n+1)
res[0] = 0
res[1] = freq[a[0]] * a[0]
for i in range(2, n+1):
    res[i] = max(res[i-2] + a[i-1] * freq[a[i-1]], res[i-1])
print(res[n])

