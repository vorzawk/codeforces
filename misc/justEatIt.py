t = int(input())
def solve():
    n = int(input())
    a = list(map(int, input().split()))
    prefixSum = 0
    for e in a:
        prefixSum += e
        if prefixSum <= 0:
            return False
    suffixSum = 0
    for e in reversed(a):
        suffixSum += e
        if suffixSum <= 0:
            return False
    return True

for _ in range(t):
    if solve():
        print("YES")
    else:
        print("NO")
