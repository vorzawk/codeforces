N = int(input())
a = list(map(int, input().split()))
n = max(a) + 1
freq = [0] * n
for e in a:
    freq[e] += 1
res = [0] * n
res[0] = 0
l = min(a)
res[l] = freq[l] * l
if max(a) == 1:
    print(res[1])
else:
    for i in range(2, n):
#        print(res, freq)
        res[i] = max(res[i-2] + i * freq[i], res[i-1])
    print(res[-1])

