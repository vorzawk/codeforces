n, k = map(int, input().split())
s = input()
c = set(input().split())
ans = 0
cnt = 0
for l in s:
    if l in c:
        cnt += 1
    else:
        ans += cnt * (cnt + 1) // 2
        cnt = 0
ans += cnt * (cnt + 1) // 2
print(ans)
