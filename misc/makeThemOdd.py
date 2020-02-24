t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    s = set()
    for elem in a:
        while elem % 2 == 0 and elem not in s:
            s.add(elem)
            elem //= 2
    print(len(s))



