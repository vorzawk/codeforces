t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    if sum(arr) % 2 == 1:
        print('YES')
        continue
    evenFlg = False
    oddFlg = False
    for e in arr:
        if e % 2 == 0 and not evenFlg:
            evenFlg = True
        if e % 2 == 1 and not oddFlg:
            oddFlg = True
    if oddFlg and evenFlg:
        print('YES')
        continue
    print('NO')


