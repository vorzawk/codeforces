from math import inf
n, a, b, c = map(int, input().split())
leastCut = min(a, b, c)
memo = {}
def solve(n):
    if n == 0:
        return 0
    if n < 0 or 0 < n < leastCut:
        return -inf
    if n in memo:
        return memo[n]
    ans = max(solve(n-c), solve(n-b), solve(n-a)) + 1
    memo[n] = ans
    return ans
print(solve(n))
