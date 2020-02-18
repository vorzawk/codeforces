def solve():
    m,s = map(int, input().split())
    if s == 0 and m == 1:
        print(0,0)
        return

    s_copy = s
    
    largestNo = [0] * m
    i = 0
    while i < m and s > 0:
        largestNo[i] += min(9,s)
        s -= min(9,s)
        i += 1
    if s != 0 or s_copy == 0:
        print(-1, -1)
        return
        
    s = s_copy - 1
    smallestNo = [0] * m
    smallestNo[0] = 1
    i = m-1
    while i < m and s > 0:
        smallestNo[i] += min(s,9)
        s -= min(s,9)
        i -= 1
    
    smallestNo = [str(d) for d in smallestNo]
    largestNo = [str(d) for d in largestNo]
    
    print(''.join(smallestNo), ''.join(largestNo))

solve()

