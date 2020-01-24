N = int(input())
for i in range(N):
    n, k = map(int, input().split())
    numCandies = n - (n % k)
    numCandies += min(n % k, k//2)
    print(numCandies)
