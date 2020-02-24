t = int(input())
for _ in range(t):
    numCandies = [int(x) for x in input().split()]
    days = 0
    while True:
        numCandies.sort(reverse=True)
        if numCandies[0] > 0 and numCandies[1] > 0:
            delta = numCandies[1] - numCandies[2]
            if delta == 0:
                delta += 1
            days += delta
            numCandies[0] -= delta
            numCandies[1] -= delta
        else:
            break
    print(days)


    
