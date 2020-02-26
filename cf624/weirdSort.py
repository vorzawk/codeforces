def solve():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    p = set(map(lambda x: int(x) - 1, input().split()))
    for i in range(1,n):
        j = i
        while j > 0 and a[j] < a[j-1]:
            if j-1 in p:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                return False
            j -= 1
    return True

t = int(input())
for _ in range(t):
    if solve():
        print("YES")
    else:
        print('NO')

