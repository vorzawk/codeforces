t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    ans = -1
    s = {a[0]}
    i = 0
    j = 1
    while i < n and j < n:
        while a[j] in s:
            if ans == -1:
                ans = j-i+1
            else:
                ans = min(ans, j-i+1)
            s.remove(a[i])
            i += 1
        s.add(a[j])
        j += 1
    print(ans)
        
    

