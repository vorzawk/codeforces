n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
badges = set()
for badge in a:
    if badge not in badges:
        badges.add(badge)
    else:
        i = 0
        while (badge + i) in badges:
            i += 1
        badges.add(badge + i)
        ans += i
print(ans)

        
